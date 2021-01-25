"""Unittest module for acme Product classes."""

import unittest
import acme


class test(unittest.TestCase):

    def test_product(self):
        """Tests product instantiation."""

        toy_name = 'Random Toy'
        toy = acme.Product(toy_name)

        self.assertIsInstance(toy, acme.Product)
        self.assertIn(toy.id, range(1000000, 10000000))
        self.assertEqual(toy.name, toy_name)
        self.assertEqual(toy.price, 10)
        self.assertEqual(toy.weight, 20)
        self.assertEqual(toy.flammability, 0.5)

        print("Output of toy.stealability()")
        toy.stealability()

        print("Output of toy.explode()")
        toy.explode()

    def test_glove(self):
        """Test instantiation of BoxingGlove."""

        glove = acme.BoxingGlove()

        self.assertEqual(glove.name, 'Boxing Glove')
        self.assertEqual(glove.weight, 10)

        print("Output of glove.explode()")
        glove.explode()

        print("Output of glove.punch()")
        glove.punch()
