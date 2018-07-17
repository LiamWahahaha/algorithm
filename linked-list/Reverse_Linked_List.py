from Node import Single_Node as node

class Solution:
    def __init__(self, list_node):
        self.list_node = list_node


    def get_len(self):
        ptr = self.list_node
        count = 0

        while ptr:
            ptr = ptr.next
            count = count + 1

        return count


    def get_kth_node(self, kth):
        ptr = self.list_node
        count = 0

        while count < kth:
            ptr = ptr.next
            count = count + 1

        return ptr


    def print_list(self, head):
        ptr = head

        while ptr:
            print(ptr.val)
            ptr = ptr.next


    def reverse_list(self):
        list_len = self.get_len()

        if list_len == 0:
            return []

        curr = self.list_node
        head = self.get_kth_node(list_len - 1)
        count = 0

        while count < list_len - 1:
            tmp = curr.next
            curr.next = head.next
            head.next = curr
            curr = tmp
            count = count + 1

        return head

def testcase():
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)

    sol = Solution(head)
    sol.print_list(sol.reverse_list())

if __name__ == '__main__':
    testcase()
