# -*- coding: utf-8 -*-
import cmd
import sys
class stack:
    def __init__(self):
        self.lists=[]

    def put(self,value):
        self.lists.append(value)

    def get(self):
        lenth = len(self.lists)
        if lenth:
            print self.lists[lenth-1]
            del self.lists[lenth-1]
        else:
            print "it is empty!"

class cstack(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.stack_set=dict()
        self.stack=""
        self.prompt=">>"
        self.intro="""
        new                栈名          新建一个栈
        put                内容名称      将一个值压入栈当中
        get                              取出栈顶的内容
        new                              新建立一个栈
        showdata                         显示当前栈的所有内容
        showstacks                       显示当前所有建立的栈
        delstack           栈名称        删除一个栈
        cd                 栈名称        切换当前栈
        exit                             推出程序
        """

    def help_exit(self):
        print "推出系统"
    
    def do_exit(self,line):
        sys.exit()


    def help_new(self):
        print "建立一个新的栈"

    def do_new(self,stackname):
        if not stackname:
           stackname = raw_input("请输入要建立的栈的名称\n")
        while stackname in self.stack_set:
           stackname = raw_input("请输入要建立的栈的名称\n")
        print  "您输入的栈的名称是: %s" % stackname
        self.stack_set[stackname]=stack()
        self.stack =stackname
        print "您当前所在的栈名称是：%s" % self.stack


    def help_put(self):
        print "将一个值压入栈当中"

    def do_put(self,value):
        if not value:
            value = raw_input("输入要压入栈的值\n")
        print "您要压入栈中的值为 %s" % value
        self.stack_set[self.stack].put(value)


    def help_get(self):
        print "从栈顶取出一个内容"
   
    def do_get(self,stack):
        self.stack_set[self.stack].get()


    def help_showdata(self):
        print "显示当前栈中的所有内容"

    def do_showdata(self,stack):
        if not len(self.stack_set):
            print "目前没有任何栈" 
        else:
            if len(self.stack_set[self.stack].lists):
                print "栈底" , self.stack_set[self.stack].lists , "栈顶"
            else:
                print "该栈为空"


    def help_showstacks(self):
        print "显示当前建立的所有栈"

    def do_showstacks(self,stack_set):
        if len(self.stack_set):
            for stack in self.stack_set:
                print stack+"  ",
            print "\n"
        else:
            print "目前没有任何栈"
            

    def help_delstack(self):
        print "删除一个栈"

    def do_delstack(self,stackname):
        if not stackname:
            stackname = raw_input("输入栈的名称\n")
        while not stackname in self.stack_set:
            self.do_showstacks('')
            stackname = raw_input("您输入的栈名称不存在，请重新输入栈的名称\n")
        del self.stack_set[stackname]
        print "栈 %s 已经删除"


    def help_cd(self):
        print "切换栈"

    def do_cd(self,stackname):
        print "当前使用的栈名是：%s" % self.stack
        if not stackname:
            stackname = raw_input("输入栈的名称\n")
        while not stackname in self.stack_set:
            self.do_showstacks('')
            stackname = raw_input("您输入的栈名称不存在，请重新输入栈的名称\n")
        self.stack=stackname
        print "已经切换当前栈为: %s" % stackname
        

    def help_prestack(self):
        print "显示当前所在的栈"

    def do_prestack(self,stack):
        print "当前所在栈为：%s" % self.stack


    do_q = do_exit

if __name__=='__main__':
    stacks=cstack()
    stacks.cmdloop()

