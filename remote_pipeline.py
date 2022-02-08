from coinstac_computation import ComputationPhase, COINSTACPyNode


class PhaseSendResults(ComputationPhase):
    def compute(self) -> dict:
        out = {"command_outputs": {}}

        for site, site_vars in self.input.items():
            out["command_outputs"][site] = site_vars["command_output"]

        out["success"] = True
        return out


remote = COINSTACPyNode(mode="remote", debug=True)
remote.add_phase(PhaseSendResults)
