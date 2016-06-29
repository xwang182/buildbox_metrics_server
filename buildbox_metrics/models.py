from django.db import models


class BuildTrain(models.Model):
    """
    One "BuildTrain" has many "Build" , one "Build" has many "Deliverable"
    Save data about a "Train". Retrived from buildbox BuildTrain class
    """
    buildbox_train_key = models.PositiveIntegerField(primary_key=True,
                                                     blank=False)
    name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)
    release_type = models.CharField(max_length=255)


class Build(models.Model):
    """
    Save data about a "Build", which belongs to a "Train".
    Retrived from buildbox Build class
    """
    buildbox_build_key = models.PositiveIntegerField(primary_key=True,
                                                     blank=False)
    train = models.ForeignKey(BuildTrain, on_delete=models.CASCADE)
    natural_number = models.PositiveIntegerField(db_index=True,
                                                 null=True, blank=True)
    status = models.CharField(max_length=255)


class Deliverable(models.Model):
    """
    Save data about a "Deliverable", which belongs to a "Build".
    data combined from buildbox Deliverable, Request and BuildStatusChange
    The time in each stage is calculated by BuildStatusChange.modified_ts
    Add the four time together to get total_build_time
    """
    buildbox_deliverable_key = models.PositiveIntegerField(primary_key=True,
                                                           blank=False)
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    deliv_type = models.CharField(max_length=255)
    variant = models.CharField(max_length=255)
    packaging_process = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    total_build_time = models.PositiveIntegerField(null=True, blank=True)
    initial_processing_time = models.PositiveIntegerField(null=True,
                                                          blank=True)
    waiting_time = models.PositiveIntegerField(null=True, blank=True)
    queued_time = models.PositiveIntegerField(null=True, blank=True)
    running_time = models.PositiveIntegerField(null=True, blank=True)
