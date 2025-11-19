from qiskit import Aer, execute
 
# Выбираем симулятор состояний квантового компьютера
backend = Aer.get_backend('qasm_simulator')
 
# Запускаем квантовую схему на симуляторе
job = execute(circuit, backend, shots=1024)
 
# Получаем результаты
result = job.result()
counts = result.get_counts(circuit)
 
print("Результаты: ", counts)