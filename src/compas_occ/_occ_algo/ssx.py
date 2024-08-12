from typing import Generator

from OCC.Core.GeomAPI import GeomAPI_IntSS

from OCC.Core.Geom import Geom_Surface


def ssx(a: Geom_Surface, b: Geom_Surface, tol=1e-7):
    """
    Parameters
    ----------
    a : Geom_Surface
        The first surface to intersect.
    b : Geom_Surface
        The second surface to intersect.
    tol : float, optional
        The tolerance value for the intersection algorithm. Default is 1e-7.

    Returns
    -------
    generator
        A generator that yields each intersection curve found between the two surfaces.
    """
    # Initialize the surface-surface intersection algorithm
    intersector = GeomAPI_IntSS(a, b, tol)

    # Check if intersection curves are found
    if intersector.IsDone() and intersector.NbLines() > 0:

        #print(f"Number of intersection curves: {intersector.NbLines()}")

        for i in range(intersector.NbLines()):
            yield intersector.Line(i + 1)



