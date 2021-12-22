# -*- coding: utf-8 -*-

#  Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
#  License: BSD 3-Clause License

class sll_node(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"node({self.val})"
    
    def __str__(self) -> str:
        """for print(node)"""
        curr = self
        res = curr.__repr__()
        while curr.next:
            curr = curr.next
            res += f" -> {curr.__repr__()}"
        return res
