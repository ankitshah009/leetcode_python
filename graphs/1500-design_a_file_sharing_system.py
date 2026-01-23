#1500. Design a File Sharing System
#Medium
#
#We will use a file-sharing system to share a very large file which consists of
#m small chunks with IDs from 1 to m.
#
#When users join the system, the system should assign a unique ID to them. The
#unique ID should be used once for each user, but when a user leaves the system,
#the ID can be reused again.
#
#Users can request a certain chunk of the file, the system should return a list
#of IDs of all the users who own this chunk. If the user receives a non-empty
#list of IDs, they receive the requested chunk successfully.
#
#Implement the FileSharing class:
#    FileSharing(int m) Initializes the object with a file of m chunks.
#
#    int join(int[] ownedChunks): A new user with a new ID joins the system with
#    a list of chunks they own. The system should assign a unique ID to the user.
#    The new user ID should be the smallest positive integer not taken by other
#    users. Return the new ID.
#
#    void leave(int userID): The user with userID leaves the system. You can
#    assume that all requests for this user are already executed.
#
#    int[] request(int userID, int chunkID): The user userID requested the chunk
#    chunkID. Return a list of the IDs of all users that own this chunk sorted
#    in ascending order.
#
#Example 1:
#Input
#["FileSharing","join","join","join","request","request","leave","request","leave","join"]
#[[4],[[1,2]],[[2,3]],[[4]],[1,3],[2,2],[1],[2,1],[2],[[]]]
#Output
#[null,1,2,3,[2],[1,2],null,[],null,1]
#Explanation
#FileSharing fileSharing = new FileSharing(4);
#fileSharing.join([1, 2]);    // user 1 joins with chunks [1, 2]
#fileSharing.join([2, 3]);    // user 2 joins with chunks [2, 3]
#fileSharing.join([4]);       // user 3 joins with chunks [4]
#fileSharing.request(1, 3);   // user 1 requests chunk 3, returns [2]
#fileSharing.request(2, 2);   // user 2 requests chunk 2, returns [1, 2]
#fileSharing.leave(1);        // user 1 leaves
#fileSharing.request(2, 1);   // user 2 requests chunk 1, returns []
#fileSharing.leave(2);        // user 2 leaves
#fileSharing.join([]);        // user with empty chunks joins, gets ID 1
#
#Constraints:
#    1 <= m <= 10^5
#    0 <= ownedChunks.length <= min(100, m)
#    1 <= ownedChunks[i] <= m
#    Values of ownedChunks are unique.
#    1 <= chunkID <= m
#    userID is guaranteed to be a user in the system if leave/request is called.
#    At most 10^4 calls will be made to join, leave, and request.
#    Each call to leave will have a matching call for join.

from typing import List
from collections import defaultdict
import heapq

class FileSharing:
    """
    Use heap for available IDs and maps for chunk ownership.
    """

    def __init__(self, m: int):
        self.m = m
        self.next_id = 1  # Next ID to assign if heap is empty
        self.available_ids = []  # Min heap of reusable IDs

        # chunk_id -> set of user_ids who own it
        self.chunk_owners = defaultdict(set)

        # user_id -> set of chunk_ids they own
        self.user_chunks = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        # Assign smallest available ID
        if self.available_ids:
            user_id = heapq.heappop(self.available_ids)
        else:
            user_id = self.next_id
            self.next_id += 1

        # Record ownership
        for chunk in ownedChunks:
            self.chunk_owners[chunk].add(user_id)
            self.user_chunks[user_id].add(chunk)

        return user_id

    def leave(self, userID: int) -> None:
        # Remove user from all chunk ownerships
        for chunk in self.user_chunks[userID]:
            self.chunk_owners[chunk].discard(userID)

        # Clear user's chunks
        del self.user_chunks[userID]

        # Make ID available for reuse
        heapq.heappush(self.available_ids, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        owners = sorted(self.chunk_owners[chunkID])

        # If someone owns it, requesting user now also owns it
        if owners:
            self.chunk_owners[chunkID].add(userID)
            self.user_chunks[userID].add(chunkID)

        return owners


class FileSharingSimple:
    """
    Simpler implementation without heap.
    """

    def __init__(self, m: int):
        self.m = m
        self.active_users = set()
        self.chunk_owners = defaultdict(set)
        self.user_chunks = {}

    def join(self, ownedChunks: List[int]) -> int:
        # Find smallest available ID
        user_id = 1
        while user_id in self.active_users:
            user_id += 1

        self.active_users.add(user_id)
        self.user_chunks[user_id] = set(ownedChunks)

        for chunk in ownedChunks:
            self.chunk_owners[chunk].add(user_id)

        return user_id

    def leave(self, userID: int) -> None:
        if userID in self.user_chunks:
            for chunk in self.user_chunks[userID]:
                self.chunk_owners[chunk].discard(userID)
            del self.user_chunks[userID]

        self.active_users.discard(userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        owners = sorted(self.chunk_owners[chunkID])

        if owners:
            self.chunk_owners[chunkID].add(userID)
            self.user_chunks[userID].add(chunkID)

        return owners


class FileSharingSortedContainer:
    """
    Using SortedList for more efficient ID management.
    """

    def __init__(self, m: int):
        from sortedcontainers import SortedList

        self.m = m
        self.available_ids = SortedList()
        self.next_id = 1
        self.chunk_owners = defaultdict(set)
        self.user_chunks = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        if self.available_ids:
            user_id = self.available_ids.pop(0)
        else:
            user_id = self.next_id
            self.next_id += 1

        for chunk in ownedChunks:
            self.chunk_owners[chunk].add(user_id)
            self.user_chunks[user_id].add(chunk)

        return user_id

    def leave(self, userID: int) -> None:
        for chunk in self.user_chunks[userID]:
            self.chunk_owners[chunk].discard(userID)

        del self.user_chunks[userID]
        self.available_ids.add(userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        owners = sorted(self.chunk_owners[chunkID])

        if owners:
            self.chunk_owners[chunkID].add(userID)
            self.user_chunks[userID].add(chunkID)

        return owners
