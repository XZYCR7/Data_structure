# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return
        #处理根节点
        root.left, root.right = root.right, root.left
        #处理左子树
        #处理右子树
        self.Mirror(root.left)
        self.Mirror(root.right)