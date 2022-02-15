from coinstac_computation import ComputationPhase, COINSTACPyNode
import subprocess
import os
import shutil


class PhaseRunPlink(ComputationPhase):
    def compute(self) -> dict:

        source_files = os.listdir("_plink")
        for file in os.listdir(self.state["baseDirectory"]):
            shutil.copy(f"{self.state['baseDirectory']}{os.sep}{file}", "_plink")
            source_files.append(file)

        args = [self.input_args["command"]]
        for k, v in self.input_args['plink_args'].items():
            args += [k, v]
        args = " ".join(" ".join(args).split())

        os.chdir("_plink")
        _ = subprocess.getoutput(args)

        for f in source_files:
            if os.path.exists(f):
                os.remove(f)

        for safe_file in [f for f in os.listdir(".") if f not in source_files]:
            shutil.copy(safe_file, self.state["transferDirectory"])
            shutil.copy(safe_file, self.state["outputDirectory"])

        return {}


local = COINSTACPyNode(mode="local", debug=True)
local.add_phase(PhaseRunPlink)
