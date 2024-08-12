from OCC.Core.GeomConvert import geomconvert

from OCC.Core.Geom import Geom_Curve,Geom_Surface,Geom_BSplineCurve,Geom_BSplineSurface
def occ_curve_to_bspline(curve:Geom_Curve)->Geom_BSplineCurve:
    return geomconvert.CurveToBSplineCurve(curve)
def occ_surf_to_bspline(surf:Geom_Surface)->Geom_BSplineSurface:
    return geomconvert.SurfaceToBSplineSurface(surf)
