## Blockchain Transaction Project

### Описание

Проект демонстрирует базовую модель транзакции в блокчейне на Python с поддержкой входов (UTXO), выходов и асимметричной цифровой подписи (RSA-PSS).

#### Основные возможности

* TxInput и TxOutput: модели для входов и выходов транзакции
* Transaction: добавление входов/выходов, сериализация, подпись и верификация
* CryptoManager: генерация пары ключей (RSA), подпись данных и проверка подписи
* Юнит-тесты для логики транзакций и криптографии


#### Требования

* Python 3.8+ 
* pip

### Установка

```bash

# Клонировать репозиторий
git clone https://github.com/narek1121/blockchain_txn_project.git
cd blockchain_txn_project

# Создать и активировать виртуальное окружение
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt

```

