"""Implied FCF growth for value-reverse-dcf. Usage:
python scripts/reverse_dcf.py EV FCF0 R [N=10] [GT=0.04]
EV and FCF0 in the same unit (INR crore). R and GT as decimals."""
import sys


def pv(g, fcf0, r, n, gt):
    flows = sum(fcf0 * (1 + g) ** t / (1 + r) ** t for t in range(1, n + 1))
    tv = fcf0 * (1 + g) ** n * (1 + gt) / (r - gt) / (1 + r) ** n
    return flows + tv


def implied_growth(ev, fcf0, r, n=10, gt=0.04, lo=-0.20, hi=0.60):
    if fcf0 <= 0 or gt >= r:
        return None
    if not pv(lo, fcf0, r, n, gt) <= ev <= pv(hi, fcf0, r, n, gt):
        return None  # outside the band
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if pv(mid, fcf0, r, n, gt) < ev else (lo, mid)
    return (lo + hi) / 2


if __name__ == "__main__":
    if len(sys.argv) < 4:
        g = implied_growth(pv(0.15, 100, 0.12, 10, 0.04), 100, 0.12)
        assert abs(g - 0.15) < 1e-6, g
        assert implied_growth(1e9, 100, 0.12) is None
        print("self-check ok")
    else:
        a = [float(x) for x in sys.argv[1:]]
        g = implied_growth(a[0], a[1], a[2], int(a[3]) if len(a) > 3 else 10, a[4] if len(a) > 4 else 0.04)
        print("outside the band" if g is None else f"implied growth {g:.2%}")
