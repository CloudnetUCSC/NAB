# VM Failure Simulation Dataset

The evaluation dataset contains a corpus of 695 time series data files simulating different VM failure scenarios,

| Dataset name | Description                                               | File count |
| ------------ | --------------------------------------------------------- | ---------- |
| Benign       | Normal state dataset that does not contain any VM failure | 152        |
| HDD          | Simulated short-term HDD failures using SCSI_debug module | 134        |
| Buffer I/O   | Simulated buffer I/O error                                | 144        |
| CPU          | CPU over-allocation failure dataset                       | 128        |
| OOM          | Out of Memory failure dataset                             | 137        |

- The _master_ branch contains the data labels for criteria-1: relaxed.
- For the data and labels of criteria-2: strict, switch to _eval-failure_ branch.

Each data file has 3 distinct regions:

- Benign region - normal state before fault injection
- Pre-failure region - after fault injection
- Post-failure region - after failure point

<table ><thead>
  <tr>
    <th rowspan="2">Dataset</th>
    <th  colspan="4" style="text-align: center">Number of Log lines</th>
  </tr>
  <tr>
    <th >Benign</th>
    <th >Pre-failure</th>
    <th >Post-failure</th>
    <th >Total</th>
  </tr></thead>
<tbody>
  <tr>
    <td >HDD</td>
    <td >79345</td>
    <td >74574</td>
    <td >10901</td>
    <td >164820</td>
  </tr>
  <tr>
    <td >OOM</td>
    <td >96833</td>
    <td >7365</td>
    <td >26196</td>
    <td >130394</td>
  </tr>
  <tr>
    <td >Buffer-IO</td>
    <td >369499</td>
    <td >97918</td>
    <td >16274</td>
    <td >483691</td>
  </tr>
  <tr>
    <td >CPU</td>
    <td >58192</td>
    <td >50187</td>
    <td >13429</td>
    <td >121808</td>
  </tr>
  <tr>
    <td >Benign</td>
    <td >113313</td>
    <td >-</td>
    <td >-</td>
    <td >113313</td>
  </tr>
  <tr>
    <td  colspan="4">Total data points</td>
    <td >1014026</td>
  </tr>
</tbody></table>
