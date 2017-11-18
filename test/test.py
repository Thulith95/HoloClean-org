

from holoclean.holoclean import HoloClean,Session
from holoclean.errordetection.errordetector import ErrorDetectors
from holoclean.featurization.featurizer import Signal_Init,Signal_cooccur,Signal_dc
from holoclean.dataset import Dataset

#import reader as dcreader
class Testing:
	def __init(self):
		pass
	def test(self):
		a=HoloClean()
		b=Session("Session",a)
		b.ingest_dataset("test/test.csv")
		b.denial_constraints("test/dc1.txt")
		err_detector=ErrorDetectors(b.Denial_constraints,a.dataengine,a.spark_session,b.dataset)
		b.add_error_detector(err_detector)
		b.ds_detect_errors()
		b.ds_domain_pruning()
		signal1=Signal_Init(b.Denial_constraints,a.dataengine,b.dataset)
		b.add_featurizer(signal1)
		signal2=Signal_cooccur(b.Denial_constraints,a.dataengine,b.dataset)
		b.add_featurizer(signal2)
		signal3=Signal_dc(b.Denial_constraints,a.dataengine,b.dataset)
		b.add_featurizer(signal3)
		b.ds_featurize()
		b._numskull()

