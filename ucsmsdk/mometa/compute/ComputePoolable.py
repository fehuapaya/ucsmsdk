"""This module contains the general information for ComputePoolable ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputePoolableConsts:
    pass


class ComputePoolable(ManagedObject):
    """This is ComputePoolable class."""

    consts = ComputePoolableConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ComputePoolable", "computePoolable", "pool-[id]", VersionMeta.Version101e, "InputOutput", 0x3f, [], ["read-only"], [u'computeBlade', u'computeRackUnit', u'computeServerUnit'], [u'computePoolPolicyRef'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []),
        "pool_dn": MoPropertyMeta("pool_dn", "poolDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "poolDn": "pool_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.pool_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputePoolable", parent_mo_or_dn, **kwargs)
