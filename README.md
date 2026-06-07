# WTMod

`wtmod` is a compiled Python package exposing water-treatment, desalination, and water-reuse process-unit models refactored from the WTMod unit blocks.

## Install

```bash
pip install wtmod
```

## Quick use

```python
from wtmod import ro_0d, nf_zo, pump

u = ro_0d.default_input()
p = ro_0d.default_params()
y = ro_0d.run(u, p)
print(y)
```

Every module exposes:

```python
run(u=None, p=None)       # returns NumPy output vector
default_input()           # default input vector
default_params()          # default parameter vector
INPUT_WIDTH, PARAM_WIDTH, OUTPUT_WIDTH
```

## Modules

- `uf_zo`: Zero-order ultrafiltration (`run`, `default_input`, `default_params`).
- `uf_physical`: Physical ultrafiltration (`run`, `default_input`, `default_params`).
- `mf_zo`: Zero-order microfiltration (`run`, `default_input`, `default_params`).
- `mf_physical`: Physical microfiltration (`run`, `default_input`, `default_params`).
- `nf_zo`: WaterTAP-style 0D nanofiltration (`run`, `default_input`, `default_params`).
- `nf_physical`: Physical nanofiltration (`run`, `default_input`, `default_params`).
- `ro_0d`: WaterTAP-style 0D reverse osmosis (`run`, `default_input`, `default_params`).
- `ro_1d`: Segmented 1D reverse osmosis (`run`, `default_input`, `default_params`).
- `ro_physical`: Physical reverse osmosis (`run`, `default_input`, `default_params`).
- `ro_2pass`: Two-stage/two-pass reverse osmosis block (`run`, `default_input`, `default_params`).
- `md_0d`: WaterTAP-style 0D direct-contact membrane distillation (`run`, `default_input`, `default_params`).
- `md_1d`: Segmented 1D direct-contact membrane distillation (`run`, `default_input`, `default_params`).
- `md_physical`: Physical membrane distillation (`run`, `default_input`, `default_params`).
- `pump`: Hydraulic pump / pressure booster (`run`, `default_input`, `default_params`).
- `energy_recovery_zo`: Zero-order pressure energy recovery (`run`, `default_input`, `default_params`).
- `mbr_zo`: Zero-order membrane bioreactor (`run`, `default_input`, `default_params`).
- `dmbr_zo`: Zero-order dynamic/reactive membrane bioreactor (`run`, `default_input`, `default_params`).


## Attribution and license

See `LICENSE` and `THIRD_PARTY_NOTICES.md`.
