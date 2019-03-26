from pmlib.anomaly_detection import AnomalyDetectionEstimator, AnomalyDetectionAssetGroupPipeline

class CustomAnomalyDetectionEstimator(AnomalyDetectionEstimator):
    def get_stages(self):
        from sklearn.covariance import (EmpiricalCovariance, EllipticEnvelope, LedoitWolf, MinCovDet, OAS, ShrunkCovariance)
        from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
        from srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
        from srom.utils.no_op import NoOp

        return [
            [
                ('skipscaling', NoOp()), 
                ('standardscaler', StandardScaler()),
                ('robustscaler', RobustScaler()), 
                ('minmaxscaling', MinMaxScaler())
            ],
            [
                # Covariance Structure based Anomaly Models
                ('empiricalcovariance', GeneralizedAnomalyModel(base_learner=EmpiricalCovariance(), fit_function='fit', predict_function='mahalanobis',score_sign=1)), 
                ('ellipticenvelope', GeneralizedAnomalyModel(base_learner=EllipticEnvelope(), fit_function='fit', predict_function='mahalanobis',score_sign=1)),
                ('ledoitwolf', GeneralizedAnomalyModel(base_learner=LedoitWolf(), fit_function='fit', predict_function='mahalanobis',score_sign=1)), 
                ('mincovdet', GeneralizedAnomalyModel(base_learner=MinCovDet(), fit_function='fit', predict_function='mahalanobis',score_sign=1)), 
                ('oas', GeneralizedAnomalyModel(base_learner=OAS(), fit_function='fit', predict_function='mahalanobis',score_sign=1)), 
                ('shrunkcovariance', GeneralizedAnomalyModel(base_learner=ShrunkCovariance(), fit_function='fit', predict_function='mahalanobis',score_sign=1)),
            ]
        ]

    
class CustomAnomalyDetectionAssetGroupPipeline(AnomalyDetectionAssetGroupPipeline):
    pass
