from direct.directnotify import DirectNotifyGlobal
from toontown.classicchars.DistributedCCharBaseAI from toontown.classicchars import DistributedCCharBaseAI

class DistributedGoofyAI(DistributedCCharBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGoofyAI")

