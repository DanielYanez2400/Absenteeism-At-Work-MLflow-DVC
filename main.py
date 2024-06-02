from src.Classifier import logger
from src.Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Classifier.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.Classifier.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.Classifier.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.Classifier.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import os

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Trainer stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/DanielYanez2400/Absenteeism-At-Work-MLflow-DVC.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'DanielYanez2400'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'e2ba9992b7f8bedcafbabcf5075e722adadc1535'

STAGE_NAME = 'Model evaluation stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e