# ETL-WEATHER
Projeto construído com o intuíto de estudar e realizar o processo de ETL (EXTRACT, TRANSFORM, LOAD) para dados recebidos de uma API de Clima, 
e armazená-los em uma banco de dados PostgreSQL. 

// Durante o desenvolvimento do projeto, o clima da cidade de São Paulo foi utilizada como exemplo.

O Projeto utiliza da linguagem Python e suas bibliotecas como: Pandas ( Para criação de data frames, e visualização dos dados brutos, para dessa forma, arrumar e limpar desorganizações ), SQLAlchemy ( Para criação da tabela do banco diretamente pelo código ), além de ferramentas como Docker e Airflow. 

Com o Docker sendo responsável por criar uma 'máquina virtual', e permitir subir o Airflow nele, para acessá-lo de forma local.
O Airflow foi utilizado para orquestrar as execuções dos processos do código, permitindo assim, um gerenciamento e definição de um timer para rodar os processos a cada determinada hora. 


