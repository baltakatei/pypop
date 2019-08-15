<!DOCTYPE html>
<meta charset="utf-8">

# Explanation of the Hancke-Kuhn Distance-Bounding Protocol

Created by [Steven Baltakatei Sandoval](https://twitter.com/baltakatei) on 2019-08-15T06:46:35Z under a [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/) license and last updated on 2019-08-15T09:30:12Z.

## Introduction

It is possible to determine how far two computers are from eachother using the speed of light and ping time. The physical distance is, at most, the ping time multiplied by the speed of light. This documents explains the [Hancke-Kuhn protocol][hancke_2005_dbp] that can calculate this upper bound for the distance between a Verifier **V** and a Prover **P** through the sending and receiving of certain bit sequences. This calculation is useful for location-based authentication technology (ex: RFID, contactless payment) defending against man-in-the middle attacks.

I have written this explanation in order to help solidify my own understanding of the protocol before I write my own implementation of it at my [GitLab repository][glbk_2019_pypop]. It is an explanation in my own words. Any errors or misrepresentations are entirely my own.

A more detailed summary with references to academic papers was published by Cristina Onete which may be found [here][onete_2012_summary] on her website's [publication page][onete_2019_publications].

This document makes use of [MathML][dis_2019_mathml] for displaying equations. [Firefox 60.0 esr][ff_2018_60esr] should render MathML symbols correctly.

## Background

### Explanation, part 1: setup

In 2005, Gerhard P. Hancke and Markus G. Kuhn [proposed][hancke_2005_dbp] a distance-bounding protocol as a defense against man-in-the-middle attacks for people who use RFID tokens in order to automatically authenticate themselves for a location-based service such as the opening of a door or purchase at a specific point-of-sale device.

An example of a man-in-the-middle attack for such a building access-control could be two attackers maliciously forwarding radio traffic between an RFID token and a building RFID reader without the RFID token owner's knowledge even in the case where the token is located at a great distance from the reader. The idea to strengthen an RFID token against such an attack is to equip the building RFID reader with some means of proving the token is physically located within a specific distance.

The goal of this project is to apply this concept to the ping time between two computers in order to prove how close the computers are from eachother. A distance-bounding protocol proof uses the distance, speed, and time equation solved for distance.

<math display='block'>
<mtext>distance</mtext>
<mo>=</mo>
<mfenced><mtext>speed</mtext></mfenced>
<mo>⋅</mo>
<mfenced><mtext>time</mtext></mfenced>
</math>

The speed is set to the speed of light since one conclusion from the theory of special relativity is that no information signal or material can travel faster than light in a vacuum. The time is set to half the ping time (round trip time divided by <math><mn>2</mn></math>.

<math display='block'>
<mtext>distance</mtext>
<mo>=</mo>
<mfenced><mtext>speed of light</mtext></mfenced>
<mo>⋅</mo>
<mfrac>
 <mfenced><mtext>ping time</mtext></mfenced>
 <mn>2</mn>
 </mfrac>
</math>

In the protocol, a verifier, **V**, and a prover, **P**, create a pair of one-time-use pseudorandom bit sequences, <math><msup><mi>R</mi><mn>0</mn></msup></math> and <math><msup><mi>R</mi><mn>1</mn></msup></math>, each containing <math><mi>n</mi></math> elements. Each element <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math> or <math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math> is a bit whose value is either <math><mn>0</mn></math> or <math><mn>1</mn></math>. These sequences can be represented like so:

<math>
 <msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup>
 <mo>=</mo>
 <mfenced>
  <msubsup><mi>R</mi><mn>1</mn><mn>0</mn></msubsup>
  <msubsup><mi>R</mi><mn>2</mn><mn>0</mn></msubsup>
  <msubsup><mi>R</mi><mn>3</mn><mn>0</mn></msubsup>
  <msubsup><mi>R</mi><mn>4</mn><mn>0</mn></msubsup>
  <msubsup><mi>R</mi><mn>5</mn><mn>0</mn></msubsup>
  <mo>⋯</mo>
  <msubsup><mi>R</mi><mi>n</mi><mn>0</mn></msubsup>
 </mfenced>
</math>

<mspace linebreak='newline' />

<math>
 <msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup>
 <mo>=</mo>
 <mfenced>
  <msubsup><mi>R</mi><mn>1</mn><mn>1</mn></msubsup>
  <msubsup><mi>R</mi><mn>2</mn><mn>1</mn></msubsup>
  <msubsup><mi>R</mi><mn>3</mn><mn>1</mn></msubsup>
  <msubsup><mi>R</mi><mn>4</mn><mn>1</mn></msubsup>
  <msubsup><mi>R</mi><mn>5</mn><mn>1</mn></msubsup>
  <mo>⋯</mo>
  <msubsup><mi>R</mi><mi>n</mi><mn>1</mn></msubsup>
 </mfenced>
</math>

Regarding these bit sequences, **V** rapidly asks **P** a stream of <math><mi>n</mi></math> questions. A question may take only one of the two forms:

  1. What is the <math><mfenced><mi>i</mi></mfenced></math>th bit of <math><msup><mi>R</mi><mn>0</mn></msup></math>, <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math>?
  
  2. What is the <math><mfenced><mi>i</mi></mfenced></math>th bit of <math><msup><mi>R</mi><mn>1</mn></msup></math>, <math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math>?

The stream of questions start with <math><mi>i</mi><mo>=</mo><mn>1</mn></math> and end with <math><mi>i</mi><mo>=</mo><mi>n</mi></math>.

In order to decide which question **V** asks **P**, **V** generates a private random bit sequence, <math><mi>C</mi></math>, which consists of <math><mi>n</mi></math> elements.  The rule **V** follows is that if <math><msub><mi>C</mi><mi>i</mi></msub><mo>=</mo>0</math> then **V** requests that **P** supply <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math>. If <math><msub><mi>C</mi><mi>i</mi></msub><mo>=</mo>1</math> then **V** requests that **P** supply <math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math>. In other words, at each round, <math><mi>i</mi></math>, **V** randomly chooses which of the two questions to ask **P**.

After sending a question to **P**, **V** records the exact time and increments <math><mi>i</mi></math> by <math><mn>1</mn></math>.

Because cause must precede effect, **P** cannot provide a correct answer to **V** until after **P** receives the question. Since the speed of light is the maximum rate at which any information can travel through space, there is a minimum ping time (or "time of flight") for any given distance between **V** and **P** which can be used by the protocol to prove an upper bound to the distance between **V** and **P**.

Immediately after receiving a question, **P** sends to **V** the value <math><msubsup><mi>R</mi><mi>i</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msubsup></math> which is the requested bit from either <math><msup><mi>R</mi><mn>0</mn></msup></math> or <math><msup><mi>R</mi><mn>1</mn></msup></math>. The set of these responses can be written as <math><msup><mi>R</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msup></math>.

Upon receiving each response, **V** records the exact time in order to calculate that particular question-response round-trip time (or "ping time").

### Example 1: how the bit sequences are used

To help explain how this process works below is an example that sets <math><mi>n</mi><mo>=</mo><mn>16</mn></math> and walks you through how to calculate the response bit sequence, <math><msup><mi>R</mi><mn><msub><mi>C</mi><mi>i</mi></msub></mn></msup></math>. 

1. Verifier **V** and Prover **P** assemble and agree upon pseudorandom bit sequences <math><msup><mi>R</mi><mn>0</mn></msup></math> and <math><msup><mi>R</mi><mn>1</mn></msup></math>

    - <math>
 <msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup>
 <mo>=</mo>
 <mfenced>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
 </mfenced>
</math>

    - <mspace linebreak='newline' /><math>
 <msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup>
 <mo>=</mo>
 <mfenced>
  <mn>1</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>1</mn>
 </mfenced>
</math>

2. Verifier **V** secretly produces a pseudorandom bit sequence <math><msub><mi>C</mi><mi>i</mi></msub></math>:

    - <math>
 <msub><mi>C</mi><mi>i</mi></msub>
 <mo>=</mo>
 <mfenced>
  <mn>0</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
 </mfenced>
</math>

3. **V** sends each bit of <math><msub><mi>C</mi><mi>i</mi></msub></math> , one at a time, starting from <math><mi>i</mi><mo>=</mo><mn>1</mn></math> until <math><mi>i</mi><mo>=</mo><mi>n</mi></math>. **V** notes the exact time when it sent each value of <math><msub><mi>C</mi><mi>i</mi></msub></math>.

4. **P** receives and uses each bit of <math><msub><mi>C</mi><mi>i</mi></msub></math> to determine whether to immediately send the bit <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math> or <math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math> to **V** in response. If all bits are received and sent without error, **P** will eventually have sent the set <math><msup><mi>R</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msup></math>.

5. **V** receives and records the arrival time for each response bit, <math><msubsup><mi>R</mi><mi>i</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msubsup></math>. **V** calculates the round-trip time for each round. The resulting values of <math><msubsup><mi>R</mi><mi>i</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msubsup></math> are:

    - <math>
 <msubsup><mi>R</mi><mi>i</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msubsup>
 <mo>=</mo>
 <mfenced>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>0</mn>
  <mn>1</mn>
  <mn>1</mn>
 </mfenced>
</math>

Below is a table illustrating how the example values for these bit sequences correlate. I have bolded the values of <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math> and <math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math> which were sent by **P** in response to the values sent of <math><msub><mi>C</mi><mi>i</mi></msub></math> sent by **V**.

<table border="1">
  <tr>
    <th><math><mi>i</mi></math></th>
    <th>01</th>
    <th>02</th>
    <th>03</th>
    <th>04</th>
    <th>05</th>
    <th>06</th>
    <th>07</th>
    <th>08</th>
    <th>09</th>
    <th>10</th>
    <th>11</th>
    <th>12</th>
    <th>13</th>
    <th>14</th>
    <th>15</th>
    <th>16</th>
  </tr>
  <tr>
    <td><math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math></td>
    <td><b>0</b><br></td>
    <td><b>1</b></td>
    <td><b>0</b></td>
    <td><b>0</b></td>
    <td>1</td>
    <td><b>0</b></td>
    <td>1</td>
    <td>1</td>
    <td><b>1</b></td>
    <td><b>0</b></td>
    <td><b>1</b></td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td><b>1</b></td>
    <td>0</td>
  </tr>
  <tr>
    <td><math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math></td>
    <td>1<br></td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td><b>1</b></td>
    <td>1</td>
    <td><b>1</b></td>
    <td><b>1</b></td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td><b>0</b></td>
    <td><b>1</b></td>
    <td><b>0</b></td>
    <td>0</td>
    <td><b>1</b></td>
  </tr>
  <tr>
    <td><math><msub><mi>C</mi><mi>i</mi></msub></math></td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>1<br></td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td><math><msubsup><mi>R</mi><mi>i</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msubsup></math></td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
  </tr>
</table>

### Explanation, part 2: False-Acceptance Rate

At each step **V** records the round trip time required between the sending of the question and the receiving of the correct answer from **P**. Given enough correct answers from **P**, **V** can then use the average value of the round trip time, <math><msub><mi>t</mi><mi>m</mi></msub></math>, of correct responses in order to calculate with some statistical certainty that **P** is physically located within a distance, <math><mi>d</mi></math>. The distance, <math><mi>d</mi></math> can be calculated using the following two equations (pg 68, [Hancke 2005][hancke_2005_dbp]).

<math display='block'>
<mi>d</mi>
<mo>=</mo>
<mi>c</mi>
<mo>⋅</mo>
<mfrac>
 <mrow><msub><mi>t</mi><mi>m</mi></msub><mo>−</mo><msub><mi>t</mi><mi>d</mi></msub></mrow>
 <mn>2</mn>
</mfrac>
</math>

<mspace linebreak='newline' />

<math display='block'>
<msub><mi>t</mi><mi>m</mi></msub><mo>=</mo><mn>2</mn><mo>⋅</mo><msub><mi>t</mi><mi>p</mi></msub><mo>+</mo><msub><mi>t</mi><mi>d</mi></msub>
</math>

In the language of the Hancke paper, variables in the two equations are defined as:

> <math><mi>c</mi></math> is the propagation speed, <math><msub><mi>t</mi><mi>p</mi></msub></math> is the one way propagation time, <math><msub><mi>t</mi><mi>m</mi></msub></math> is the measured total round-trip time, and <math><msub><mi>t</mi><mi>d</mi></msub></math> is the processing delay of the remote device.

A conservative practice defines <math><msub><mi>t</mi><mi>d</mi></msub><mo>=</mo><mn>0</mn></math> for the processing delay variable. It is conservative because <math><msub><mi>t</mi><mi>d</mi></msub></math> is a function of the capabilities of the hardware **P** uses to process requests from **V**. If both **P** and **V** trust eachother to use specific hardware with consistent and accurate estimates for response times then <math><msub><mi>t</mi><mi>d</mi></msub></math> may be specified. However, the Hancke protocol-Kuhn does not provide a means for proving or incentivizing **P** to accurately measure and report its own hardware capability.

The highest possible propagation speed, <math><mi>c</mi></math>, according to the laws of physics is the speed of light in a vacuum. According to section 2.1.1.1 of the 8th edition of the [International System of Units][bipm_2006_si], a document published by the International Bureau of Weights and Measures, this speed is <math><mn>299 792 458</mn><mfrac><mi>m</mi><mi>s</mi></mfrac></math>.

The statistical certainty that the round-trip time between **P** and **V** is less than <math><msub><mi>t</mi><mi>m</mi></msub></math> is <math><mfenced><mrow><mn>1</mn><mo>−</mo><msub><mi>p</mi><mtext>FA</mtext></msub></mrow></mfenced></math> where <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> is the "false-accept probability". The value of <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> must be a statistical estimate constrained by the possibility that prover, **P**, maliciously sends its best guesses before receiving the questions from **V**. If **P** dishonestly wishes to convince **V** that the distance is lower than it really is, then **P** can achieve a <math><mfrac><mn>3</mn><mn>4</mn></mfrac></math> probability of guessing correctly for a given round without having yet received that round's value of <math><msub><mi>C</mi><mi>i</mi></msub></math>. This is because, on average, half of the rounds do not require guessing at all since half the time <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup><mo>=</mo><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math>. The other half of the time **P**'s best strategy, assuming **V** generated <math><mi>C</mi></math> securely, is to guess <math><mn>1</mn></math> or <math><mn>0</mn></math> at random.

The false acceptance probability, or "False-Acceptance Rate", <math><msub><mi>p</mi><mtext>FA</mtext></msub></math>, of **V** accepting the distance-bounding protocol proof of **P** can be calculated using the following equation found on the sixth page of the [Hancke paper][hancke_2005_dbp]. This equation calculates <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> assuming **V** judges that receiving <math><mi>k</mi></math> correct responses out of <math><mi>n</mi></math> total rounds is acceptable.

<math display='block'>
<msub>
 <mi>p</mi>
 <mtext>FA</mtext>
</msub>
<mo>=</mo>
<munderover>
 <mo>∑</mo>
  <mrow>
   <mi>i</mi>
   <mo>=</mo>
   <mi>k</mi>
  </mrow>
  <mi>n</mi>
</munderover>
<mfenced>
 <mfrac linethickness="0">
  <mi>n</mi>
  <mi>i</mi>
 </mfrac>
</mfenced>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>3</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mi>i</mi>
</msup>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>1</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mrow>
  <mi>n</mi>
  <mo>−</mo>
  <mi>i</mi>
 </mrow>
</msup>

</math>

The equation states that <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> is equal to the sum of each individual probability where **P** guessed correctly <math<mi>k</mi></math> or more times (for example: one outcome exists where **P** guesses perfectly, some outcomes where **P** makes only one mistake, some outcomes where **P** makes two mistakes, etc.). The total number of terms in the sum is of <math><mi>n</mi><mo>−</mo><mi>k</mi><mo>+</mo><mn>1</mn></math>. 

In other words, the final term (the <math><mfenced><mi>n</mi></mfenced></math>'th term) of the sum is the probability that **P** guesses correctly in exactly every single response (one very rare possibility). The penultimate term (the <math><mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></mfenced></math>'th term) is the probability that **P** guesses correctly every single time *except* for exactly *one* mistake somewhere (a slightly less rare possibility). The <math><mfenced><mrow><mi>n</mi><mo>−</mo><mn>2</mn></mrow></mfenced></math>'th term is the probability that **P** guesses all responses correctly but with *two* errors somewhere. The <math><mfenced><mrow><mi>n</mi><mo>−</mo><mn>3</mn></mrow></mfenced></math>'th term is the probability that **P** guesses all responses correctly but with *three* errors somewhere, and so forth. The first term of the sum is the probability that **P** guesses correctly exactly <math><mi>k</mi></math> times out of <math><mi>n</mi></math> responses and therefore provided incorrect responses exactly <math><mfenced><mrow><mi>n</mi><mo>−</mo><mi>k</mi></mrow></mfenced></math> times. Each term of the sum is the [binomial probability function][wp_2019_bdf] (a.k.a. "binomial distribution formula" or "probability mass function") which should be part of the syllabus for any a typical Statistics course.

Since no factor of the equation for <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> can be made exactly equal to zero it is impossible for Verifier **V** to completely eliminate the possibility that **P** could forge this distance-bounding proof. The best **V** can do to strengthen confidence in the proof's validity is to set the parameters <math><mi>k</mi></math> and <math><mi>n</mi></math> to values that produce an acceptably low value for <math><msub><mi>p</mi><mtext>FA</mtext></msub></math>, the probability of falsely accepting a maliciously constructed proof by Prover **P**.

### Example 2: Calculating False-Acceptance Rate

Below is a copy of the previous example table but with values of <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math> and <math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math> bolded when <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup><mo>=</mo><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math>. From inspection it should be clear that **P** does not have to guess roughly half of the rounds since a quarter of the time <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup><mo>=</mo><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup><mo>=</mo><mn>0</mn></math> and a quarter of the time <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup><mo>=</mo><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup><mo>=</mo><mn>1</mn></math>.

<table border="1">
  <tr>
    <th><math><mi>i</mi></math></th>
    <th>01</th>
    <th>02</th>
    <th>03</th>
    <th>04</th>
    <th>05</th>
    <th>06</th>
    <th>07</th>
    <th>08</th>
    <th>09</th>
    <th>10</th>
    <th>11</th>
    <th>12</th>
    <th>13</th>
    <th>14</th>
    <th>15</th>
    <th>16</th>
  </tr>
  <tr>
    <td><math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup></math></td>
    <td>0<br></td>
    <td>1</td>
    <td><b>0</b></td>
    <td><b>0</b></td>
    <td><b>1</b></td>
    <td>0</td>
    <td><b>1</b></td>
    <td><b>1</b></td>
    <td>1</td>
    <td>0</td>
    <td><b>1</b></td>
    <td>1</td>
    <td>0</td>
    <td><b>0</b></td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td><math><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math></td>
    <td>1<br></td>
    <td>0</td>
    <td><b>0</b></td>
    <td><b>0</b></td>
    <td><b>1</b></td>
    <td>1</td>
    <td><b>1</b></td>
    <td><b>1</b></td>
    <td>0</td>
    <td>1</td>
    <td><b>1</b></td>
    <td>0</td>
    <td>1</td>
    <td><b>0</b></td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td><math><msub><mi>C</mi><mi>i</mi></msub></math></td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>1<br></td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td><math><msubsup><mi>R</mi><mi>i</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msubsup></math></td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
  </tr>
</table>

Side note: I believe the inefficiency of allowing the protocol to have instances where <math><msubsup><mi>R</mi><mi>i</mi><mn>0</mn></msubsup><mo>=</mo><msubsup><mi>R</mi><mi>i</mi><mn>1</mn></msubsup></math> is due to Hancke designing the protocol to be simple in order to accomodate implementation in RFID tags with limited computatioinal ability and over noisy communication channels. The scope of my [Proof of Ping project][glbk_2019_pypop] doesn't include attempting to improve the protocol but to simply implement it as described in the Hancke paper.

In order to illustrate how the False-Acceptance Rate, <math><msub><mi>p</mi><mtext>FA</mtext></msub></math>, is calculated, let us say that **V** was programmed to accept <math><mn>14</mn></math> correct responses out of <math><mn>16</mn></math> (<math><mi>k</mi><mo>=</mo><mn>14</mn></math>, <math><mi>n</mi><mo>=</mo><mn>16</mn></math>). For this case the calculation of <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> is detailed in [this spreadsheet file][bk_20190815_pfacalc] (in [ODS format][wp_2019_opendocument]) as well directly below.

The binomial coefficient factor in the <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> equation can be expanded out, with <math><mo>!</mo></math> signifying the factorial operation (for example, <math><mn>5</mn><mo>!</mo><mo>=</mo><mn>5</mn><mo>⋅</mo><mn>4</mn><mo>⋅</mo><mn>3</mn><mo>⋅</mo><mn>2</mn><mo>⋅</mo><mn>1</mn><mo>=</mo><mn>120</mn></math>).

<math display='block'>
<msub>
 <mi>p</mi>
 <mtext>FA</mtext>
</msub>
<mo>=</mo>
<munderover>
 <mo>∑</mo>
  <mrow>
   <mi>i</mi>
   <mo>=</mo>
   <mi>k</mi>
  </mrow>
  <mi>n</mi>
</munderover>
<mfenced>
 <mfrac>
  <mrow>
   <mi>n</mi>
   <mo>!</mo>
  </mrow>
  <mrow>
   <mi>i</mi>
   <mo>!</mo>
   <mfenced>
    <mrow>
	 <mi>n</mi>
	 <mo>−</mo>
	 <mi>i</mi>
	</mrow>
   </mfenced>
   <mo>!</mo>
  </mrow>
 </mfrac>
</mfenced>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>3</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mi>i</mi>
</msup>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>1</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mrow>
  <mi>n</mi>
  <mo>−</mo>
  <mi>i</mi>
 </mrow>
</msup>
</math>

The sum consists consist of a total of <math><mi>n</mi><mo>−</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>16</mn><mo>−</mo><mn>14</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn></math> terms.

The last term (<math><mi>i</mi><mo>=</mo><mi>n</mi><mo>=</mo><mn>16</mn></math>) is:

<math display='block'>
<mfenced>
 <mfrac>
  <mrow>
   <mn>16</mn>
   <mo>!</mo>
  </mrow>
  <mrow>
   <mn>16</mn>
   <mo>!</mo>
   <mfenced>
    <mrow>
	 <mn>16</mn>
	 <mo>−</mo>
	 <mn>16</mn>
	</mrow>
   </mfenced>
   <mo>!</mo>
  </mrow>
 </mfrac>
</mfenced>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>3</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mn>16</mn>
</msup>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>1</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mrow>
  <mn>16</mn>
  <mo>−</mo>
  <mn>16</mn>
 </mrow>
</msup>
<mo>=</mo>
<mn>1.00226</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-2</mn>
</msup>
</math>

The penultimate term (<math><mi>i</mi><mo>=</mo><mn>15</mn></math>) is:

<math display='block'>

<mfenced>
 <mfrac>
  <mrow>
   <mn>16</mn>
   <mo>!</mo>
  </mrow>
  <mrow>
   <mn>15</mn>
   <mo>!</mo>
   <mfenced>
    <mrow>
	 <mn>16</mn>
	 <mo>−</mo>
	 <mn>15</mn>
	</mrow>
   </mfenced>
   <mo>!</mo>
  </mrow>
 </mfrac>
</mfenced>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>3</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mn>15</mn>
</msup>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>1</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mrow>
  <mn>16</mn>
  <mo>−</mo>
  <mn>15</mn>
 </mrow>
</msup>

<mo>=</mo>
<mn>5.34538</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-2</mn>
</msup>

</math>

The first term (<math><mi>i</mi><mo>=</mo><mi>k</mi><mo>=</mo><mn>14</mn></math>) is:

<math display='block'>

<mfenced>
 <mfrac>
  <mrow>
   <mn>16</mn>
   <mo>!</mo>
  </mrow>
  <mrow>
   <mn>14</mn>
   <mo>!</mo>
   <mfenced>
    <mrow>
	 <mn>16</mn>
	 <mo>−</mo>
	 <mn>14</mn>
	</mrow>
   </mfenced>
   <mo>!</mo>
  </mrow>
 </mfrac>
</mfenced>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>3</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mn>14</mn>
</msup>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>1</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mrow>
  <mn>16</mn>
  <mo>−</mo>
  <mn>14</mn>
 </mrow>
</msup>

<mo>=</mo>
<mn>1.33635</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-1</mn>
</msup>

</math>

The sum of these three terms is:

<math display='block'>

<mn>1.00226</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-2</mn>
</msup>

<mo>+</mo>

<mn>5.34538</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-2</mn>
</msup>

<mo>+</mo>

<mn>1.33635</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-1</mn>
</msup>

<mo>=</mo>
<mn>1.97111</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-1</mn>
</msup>

</math>

Therefore, the False-Acceptance Rate, <math><msub><mi>p</mi><mtext>FA</mtext></msub></math> can be written as:

<math display='block'>
<msub>
 <mi>p</mi>
 <mtext>FA</mtext>
</msub>
<mo>=</mo>
<munderover>
 <mo>∑</mo>
  <mrow>
   <mi>i</mi>
   <mo>=</mo>
   <mi>k</mi>
   <mo>=</mo>
   <mi>14</mi>
  </mrow>
  <mrow>
   <mi>n</mo>
   <mo>=</mo>
   <mi>16</mi>
  </mrow>
</munderover>
<mfenced>
 <mfrac>
  <mrow>
   <mi>n</mi>
   <mo>!</mo>
  </mrow>
  <mrow>
   <mi>i</mi>
   <mo>!</mo>
   <mfenced>
    <mrow>
	 <mi>n</mi>
	 <mo>−</mo>
	 <mi>i</mi>
	</mrow>
   </mfenced>
   <mo>!</mo>
  </mrow>
 </mfrac>
</mfenced>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>3</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mi>i</mi>
</msup>
<mo>⋅</mo>
<msup>
 <mfenced>
  <mfrac>
   <mn>1</mn>
   <mn>4</mn>
  </mfrac>
 </mfenced>
 <mrow>
  <mi>n</mi>
  <mo>−</mo>
  <mi>i</mi>
 </mrow>
</msup>

<mo>=</mo>
<mn>1.97111</mn>
<mo>⋅</mo>
<msup>
 <mn>10</mn>
 <mn>-1</mn>
</msup>

<mo>=</mo>
<mn>19.7111</mn>
<mo>%</mo>

</math>

In other words, if **V** decides to accept only <math><mi>k</mi><mo>=</mo><mn>14</mn></math> or more correct bits from from **P** out of a possible <math><mi>n</mi><mo>=</mo><mn>16</mn></math> bits in the bit sequences they exchange, then there is about a <math><mn>19.7</mn><mo>%</mo></math> chance that **P** could fool **V** into accepting that the distance between them was lower than it physically is. **P** could do this by completely disregarding **V**'s questions, <math><mi>C</mi></math>, and sending only best guesses for bit sequence <math><msup><mi>R</mi><mi><msub><mi>C</mi><mi>i</mi></msub></mi></msup></math> given the structure of <math><msup><mi>R</mi><mn>0</mn></msup></math> and <math><msup><mi>R</mi><mn>1</mn></msup></math>.

[hancke_2005_dbp]: https://web.archive.org/web/20170810181543/http://www.cl.cam.ac.uk/~mgk25/sc2005-distance.pdf

[eforbes_20170415_udppython]: https://tutorialedge.net/python/udp-client-server-python/

[wp_2019_dbp]: https://en.wikipedia.org/wiki/Distance-bounding_protocol

[bipm_2006_si]: https://web.archive.org/web/20190810173159/https://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf

[wp_2019_bdf]: https://en.wikibooks.org/wiki/Statistics/Distributions/Binomial

[dis_2019_mathml]: http://danielscully.co.uk/projects/mathml-guide/browsertest.php

[ff_2018_60esr]: https://www.mozilla.org/en-US/firefox/60.0esr/releasenotes/

[onete_2012_summary]: http://onete.net/papers/DistBound.pdf

[glbk_2019_pypop]: https://gitlab.com/baltakatei/pypop

[onete_2019_publications]: https://www.onete.net/publications.html

[bk_20190815_pfacalc]: http://reboil.com/calc/0020190815T091844Z..false_accept_probability_calc_table.ods

[wp_2019_opendocument]: https://en.wikipedia.org/wiki/OpenDocument

<hr>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="🅭🅯🄯4.0" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
