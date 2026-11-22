# گزارش اجرای واقعی

اجرا با Python 3.12.14 در 2026-11-22T09:40:50.884657+00:00 روی Linux.

```text
$ python gradient_demo.py
{
  "x": 10,
  "target": 30,
  "weight_before": 2,
  "learning_rate": 0.001,
  "prediction_before": 20,
  "loss_before": 100,
  "gradient": -200,
  "weight_after": 2.2,
  "prediction_after": 22.0,
  "loss_after": 64.0
}
Exit status: 0
```

```text
$ python -m unittest discover -s . -v
test_assignment_values_and_one_update (test_gradient_demo.GradientDemoTests.test_assignment_values_and_one_update) ... ok
test_gradient_agrees_with_independent_finite_difference (test_gradient_demo.GradientDemoTests.test_gradient_agrees_with_independent_finite_difference) ... ok
test_large_step_can_increase_loss (test_gradient_demo.GradientDemoTests.test_large_step_can_increase_loss) ... ok
test_optimal_weight_has_zero_gradient_and_remains_fixed (test_gradient_demo.GradientDemoTests.test_optimal_weight_has_zero_gradient_and_remains_fixed) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
Exit status: 0
```

```text
$ python -m compileall -q gradient_demo.py test_gradient_demo.py

Exit status: 0
```

هر چهار آزمون موفق شدند. مشتق تحلیلی با تفاضل مرکزیِ مستقل کنترل شد و اثر نرخ یادگیری بزرگ‌تر نیز بررسی شد.

این اجرا محاسبهٔ سؤال دوم را بازتولید می‌کند. تعمیم مدل واقعی روی دادهٔ جدید به داده و ارزیابی مستقل نیاز دارد. آزمون‌ها شاهدی دربارهٔ اجرای پروژهٔ .NET سؤال چهارم یا رفتار واقعی BlogSpecLab سؤال پنجم ارائه نمی‌کنند.

بازبینی پاسخ‌ها شامل پوشش پنج سؤال، مقایسه با اسلایدها، صحت فرمول‌ها و بررسی لینک‌های داخلی مخزن بود. خروجی کلاس به‌عنوان منبع معرفی شده و مثال‌ها و فرض‌های تکمیلی در متن مشخص شده‌اند.