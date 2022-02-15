import coinstac

from local_pipeline import local
from coinstac_computation import PhaseEndWithSuccess, COINSTACPyNode

remote = COINSTACPyNode(mode="remote", debug=True)
remote.add_phase(PhaseEndWithSuccess)

coinstac.start(local, remote)
