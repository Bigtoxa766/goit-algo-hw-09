# goit-algo-hw-09

    Жадібний алгоритм є більш ефективним у плані часу виконання та просторової складності, особливо для великих сум. Однак він не завжди дає оптимальне рішення, особливо якщо номінали монет не є кратними.

    Алгоритм динамічного програмування є гарантовано оптимальним для будь-якої системи монет, але його часові витрати зростають лінійно зі збільшенням суми. Це робить його менш продуктивним для дуже великих сум, але незамінним у випадках, коли жадібний алгоритм не здатний знайти оптимальне рішення.

Отже, вибір між цими алгоритмами залежить від конкретної ситуації:

    Якщо валюта складається з номіналів, що є кратними, і ви працюєте з великими сумами, жадібний алгоритм — найкращий вибір.

    Якщо потрібно гарантувати мінімальну кількість монет для складної системи номіналів, алгоритм динамічного програмування забезпечить оптимальний результат, хоча й потребуватиме більше часу.