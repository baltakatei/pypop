<!DOCTYPE html>
<meta charset="utf-8">

# 🛎 Proof of Ping

An implementation of a distance-bounding protocol


## Objective

Create a `python3` script that enables a user to calculate the an upper bound of physical distance to another user using time-of-flight and the speed of light.


## Background

It is possible using round-trip time (ping time) between a Verifier and a Prover and the assumption that nothing can travel faster than the speed of light in order to calculate an upper bound for distance between the Verifier and Prover.

Such a distance-bounding method is described in the [Hancke-Kuhn Protocol][hancke_2005_dbp]. See this [explanation of this protocol](http://reboil.com/blog/0020190815T064636Z..hancke-kuhn_dbp_explanation.html).


## Method

This project will implement the [Hancke-Khun distance-bounding protocol][hancke_2005_dbp] in `python3`.


## References

* Reference 1. ["An RFID Distance Bounding Protocol" by Gerard P. Hancke and Markus G. Kuhn, 2005, IEEE][hancke_2005_dbp]

* Reference 2. Sending and receiving UDP packets in python ([link][eforbes_20170415_udppython])

* Reference 3. Wikipedia article on distance-bounding protocol ([link][wp_2019_dbp])


[hancke_2005_dbp]: https://web.archive.org/web/20170810181543/http://www.cl.cam.ac.uk/~mgk25/sc2005-distance.pdf

[eforbes_20170415_udppython]: https://tutorialedge.net/python/udp-client-server-python/

[wp_2019_dbp]: https://en.wikipedia.org/wiki/Distance-bounding_protocol

[bipm_2006_si]: https://web.archive.org/web/20190810173159/https://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf

[wp_2019_bdf]: https://en.wikibooks.org/wiki/Statistics/Distributions/Binomial

