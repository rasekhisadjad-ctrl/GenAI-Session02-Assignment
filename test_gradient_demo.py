import unittest

from gradient_demo import squared_loss, training_step


class GradientDemoTests(unittest.TestCase):
    def test_assignment_values_and_one_update(self):
        result = training_step(x=10, target=30, weight=2, learning_rate=0.001)
        self.assertEqual(result.prediction_before, 20)
        self.assertEqual(result.loss_before, 100)
        self.assertEqual(result.gradient, -200)
        self.assertAlmostEqual(result.weight_after, 2.2)
        self.assertAlmostEqual(result.prediction_after, 22)
        self.assertAlmostEqual(result.loss_after, 64)

    def test_gradient_agrees_with_independent_finite_difference(self):
        x, target, weight, epsilon = 10, 30, 2, 1e-6
        upper_loss = squared_loss((weight + epsilon) * x, target)
        lower_loss = squared_loss((weight - epsilon) * x, target)
        estimated_gradient = (upper_loss - lower_loss) / (2 * epsilon)
        actual = training_step(x, target, weight, learning_rate=0.001).gradient
        self.assertAlmostEqual(actual, estimated_gradient, places=5)

    def test_large_step_can_increase_loss(self):
        result = training_step(x=10, target=30, weight=2, learning_rate=0.02)
        self.assertEqual(result.weight_after, 6)
        self.assertEqual(result.loss_after, 900)
        self.assertGreater(result.loss_after, result.loss_before)

    def test_optimal_weight_has_zero_gradient_and_remains_fixed(self):
        result = training_step(x=10, target=30, weight=3, learning_rate=0.001)
        self.assertEqual(result.loss_before, 0)
        self.assertEqual(result.gradient, 0)
        self.assertEqual(result.weight_after, 3)


if __name__ == "__main__":
    unittest.main()
