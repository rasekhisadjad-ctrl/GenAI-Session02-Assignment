"""Reproduce question 2 with scalar arithmetic and one gradient descent step."""

from dataclasses import asdict, dataclass
import json


@dataclass(frozen=True)
class StepResult:
    x: float
    target: float
    weight_before: float
    learning_rate: float
    prediction_before: float
    loss_before: float
    gradient: float
    weight_after: float
    prediction_after: float
    loss_after: float


def squared_loss(prediction: float, target: float) -> float:
    return (prediction - target) ** 2


def training_step(x: float, target: float, weight: float, learning_rate: float) -> StepResult:
    prediction = weight * x
    loss = squared_loss(prediction, target)

    # Backpropagation through prediction = weight * x, using the chain rule.
    loss_gradient_at_prediction = 2 * (prediction - target)
    gradient = loss_gradient_at_prediction * x

    # One update by the gradient descent optimizer.
    updated_weight = weight - learning_rate * gradient
    updated_prediction = updated_weight * x
    updated_loss = squared_loss(updated_prediction, target)

    return StepResult(
        x=x,
        target=target,
        weight_before=weight,
        learning_rate=learning_rate,
        prediction_before=prediction,
        loss_before=loss,
        gradient=gradient,
        weight_after=updated_weight,
        prediction_after=updated_prediction,
        loss_after=updated_loss,
    )


def main() -> None:
    result = training_step(x=10, target=30, weight=2, learning_rate=0.001)
    print(json.dumps(asdict(result), indent=2))


if __name__ == "__main__":
    main()
