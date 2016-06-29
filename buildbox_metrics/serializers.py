from rest_framework import serializers
from buildbox_metrics.models import BuildTrain, Build, Deliverable


class BuildTrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildTrain
        fields = ('buildbox_train_key', 'name',
                  'product_name', 'codename', 'release_type')


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('buildbox_build_key', 'train', 'natural_number', 'status')


class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverable
        fields = ('buildbox_deliverable_key', 'build', 'deliv_type',
                  'variant', 'packaging_process', 'status',
                  'total_build_time', 'initial_processing_time',
                  'waiting_time', 'queued_time', 'running_time')
