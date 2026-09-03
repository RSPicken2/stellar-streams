# MISCADA 2025-26 Final Project

This repo stores all the jupyter notebookes used to analise the 43 Nbody simulations I performed for my final assessment. The following sections give each notebook a brief description.

## EscapersAnalysis
Covers my modelling of the tidal radius and how that relates to the amount of mass escaping from the Globular Cluster (GC)

## GlobularClusters
This is mostly used to show images of the clusters as they evolve (and me just playing around)

## HyadesValidate
This contains the comparison of our simulation recreating the Hyades Stream and the Meingast (2019) data for current star positions.

## InitialConditionsFinder
Used to perform some Galpy integrations to estimate what initial velocities I would need to give the cluster to produce different eccentric orbits with different periapses.

## MakeTimestepDF
Used to create an index of simulation snapshots once to make reading them easier later

## MassProfileAnalysis
Used to graph the mass profiles of clusters and for some performance benchmarking

## Ridgeline
Originally named after trying to find the central 'ridge' defining the shape of the cluster. I didn't persue this up to the final paper so this was mostly reused to focus on the stream's lengths, widths and densities. 

## ShrinkingSpere
Testing the shrinking sphere approach to finding the centre of clusters

## StreamAnalysis
Testing how to filter streams away from other particles that have escaped far from the cluster

## utils
The various utils notebooks store functions various other notebooks need to run.

## experiments.py
Defining each of the simulation groups

## plotparams.py
Plot formatting provided by Sownak Bose

## potentials.py
Reproducing the potential model in Nody6++GPU to help calculate the tidal radius in Escapers.ipynb