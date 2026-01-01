"""airflow minimal DAG definition.

Place this file in your Airflow dags folder.
Running it directly will only construct the DAG if airflow is installed.
"""

def main():
    try:
        from airflow import DAG
        from airflow.operators.python import PythonOperator
        from datetime import datetime
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return

    def hello():
        print("hello from airflow task")

    with DAG(
        dag_id="sm0l_demo_dag",
        start_date=datetime(2024, 1, 1),
        schedule_interval="@daily",
        catchup=False,
        tags=["sm0l"],
    ) as dag:
        PythonOperator(task_id="hello", python_callable=hello)

    print("DAG id:", dag.dag_id)

if __name__ == "__main__":
    main()
