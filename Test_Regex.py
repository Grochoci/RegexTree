from regextree import Stack, RegexTree, regex_match
from regextreenode import RegexTreeNode, UnaryNode, \
    BinaryNode, DotNode, BarNode, StarNode
import unittest


class TestRegexTree(unittest.TestCase):

    def test_e(self):
        ''' Testing with e.'''
        r = RegexTree("e")
        s = r.root
        self.assertEqual(str(s), str(RegexTreeNode('e', [])))
        
    def test_1(self):
        ''' Testing with 1.'''
        r = RegexTree("1")
        s = r.root
        self.assertEqual(str(s), str(RegexTreeNode('1', [])))
        
    def test_0(self):
        ''' Testing with 0.'''
        r = RegexTree("0")
        s = r.root
        self.assertEqual(str(s), str(RegexTreeNode('0', [])))
    
    def test_star_e(self):
        ''' Testing with e*.'''
        r = RegexTree("e*")
        s = r.root
        self.assertEqual(str(s), str(StarNode(RegexTreeNode('e', []))))
        
    def test_star_1(self):
        ''' Testing with 1*.'''
        r = RegexTree("1*")
        s = r.root
        self.assertEqual(str(s), str(StarNode(RegexTreeNode('1', []))))

    def test_star_0(self):
        ''' Testing with 0*.'''
        r = RegexTree("0*")
        s = r.root
        self.assertEqual(str(s), str(StarNode(RegexTreeNode('0', []))))
        
    def test_bar_0_1(self):
        ''' Testing with 0|1'''
        r = RegexTree("(0|1)")
        s = r.root
        self.assertEqual(str(s), str(BarNode(RegexTreeNode('0', []),
                                             RegexTreeNode('1', []))))

    def test_bar_e_1(self):
        ''' Testing with e|1'''
        r = RegexTree("(e|1)")
        s = r.root
        self.assertEqual(str(s), str(BarNode(RegexTreeNode('e', []),
                                             RegexTreeNode('1', []))))

    def test_dot_1_0(self):
        ''' Testing with 1.0'''
        r = RegexTree("(1.0)")
        s = r.root
        self.assertEqual(str(s), str(DotNode(RegexTreeNode('1', []),
                                             RegexTreeNode('0', []))))
    
    def test_dot_1_e(self):
        ''' Testing with 1.e'''
        r = RegexTree("(1.e)")
        s = r.root
        self.assertEqual(str(s), str(DotNode(RegexTreeNode('1', []),
                                             RegexTreeNode('e', []))))
    
    def test_bar_star(self):
        ''' Testing with 0*|1*'''
        r = RegexTree("(0*|1*)")
        s = r.root
        self.assertEqual(str(s), str(BarNode(StarNode(RegexTreeNode('0',
                                [])), StarNode(RegexTreeNode('1', [])))))
    
    def test_dot_dot(self):
        ''' Testing with (0.1).0'''
        r = RegexTree("((0.1).0)")
        s = r.root
        self.assertEqual(str(s), str(DotNode(DotNode(RegexTreeNode('0',
                []), RegexTreeNode('1', [])), RegexTreeNode('0', []))))

    def test_complete(self):
        ''' Testing with all Nodes'''
        r = RegexTree("((1.(0|1)*).0)")
        s = r.root
        self.assertEqual(str(s), str(DotNode(DotNode(RegexTreeNode('1',
            []), StarNode(BarNode(RegexTreeNode('0', []), RegexTreeNode(
                '1', [])))), RegexTreeNode('0', []))))
       
    
class TestRegexMatch(unittest.TestCase):
    
    def test_1_1(self):
        ''' Testing with r = 1, s = 1.'''
        r = RegexTree("1")
        self.assertTrue((regex_match(r, "1")))
        
    def test_1(self):
        r = RegexTree("(0.(1|0))*")
        self.assertTrue((regex_match(r, "010001")))
        
    def test_2(self):
        r = RegexTree("(0.(1|e))*")
        self.assertTrue((regex_match(r, "000")))
    
    def test_3(self):
        r = RegexTree("(1.(0.1)*)")
        self.assertTrue((regex_match(r, "10101")))
    
    def test_4(self):
        r = RegexTree("(0.(0|(1.0))*)")
        self.assertTrue((regex_match(r, "001010")))
         
unittest.main(exit=False)