results=./results
rep_history=./final-report/history
report=./final-report

echo "Удаляем старую папку с результатами: $results"
rm -rf "$results"

echo "Запускаем тесты с генерацией результатов в $results"
pytest --alluredir="$results"

echo "Переносим историю из $rep_history в $results"
if [ -d "$rep_history" ]; then
  mv "$rep_history" "$results"

echo "Удаляем старую папку с отчетом: $report"
rm -rf "$report"

echo "Генерируем Allure отчет в $report"
allure generate "$results" -o "$report" --clean

echo "Открываем отчет в браузере"
allure open "$report"
