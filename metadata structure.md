The metadata required for each dataset will vary based on the governance framework established on a project-by-project basis.

| OBO | Shorthand | Modifier | Type | Description (from Contributor) | Evidence (from Consumer) |
| --- | --- | --- | --- | --- | --- |
| DUO_0000043 | CC | Clinical Care Use | Boolean | 
| DUO_0000020 | COL | Collaboration Required | String | PI Contact information required | Agree to terms |
| DUO_0000007 | DS | Disease Specific Research | String | Provide detail [DOID] or [MONDO] | User must describe disease-specific research use in IDU statement |
| DUO_0000021 | IRB | Ethics Approval Required | Boolean |  | User prompted to provide IRB/IEC approval |
| DUO_0000042 | GRU | General Research Use | Boolean | | Agree to terms |
| DUO_0000016 | GSO | Genetic Studies Only | Boolean | | Agree to terms |
| DUO_0000022 | GS | Geographical Restriction | String | Provide country restriction [ISO 3166⍺2] | Access limited to users within region |
| DUO_0000006 | HMB | Health or Medical or Biomedical Research | Boolean | | Agree to terms |
| DUO_0000028 | IS | Institution Specific Restriction | String | Name Institution [ror.org] | Access limited to users within institution |
| DUO_0000015 | NMDS | No General Methods Research | Boolean | | Agree to terms |
| DUO_0000004 | NRES | No Restriction | Boolean | | Data is available under Open or Anonymous access |
| DUO_0000018 | NPUNCU | Not-for-Profit, Non-Commercial Use Only | Boolean | | Access limited to NPO; Agree to terms |
| DUO_0000046 | NCU | Non-Commercial Use Only | Boolean | | Agree to terms | 
| DUO_0000045 | NPU | Not-for-Profit Organisation Use Only | Boolean | | Access limited to NPO |
| DUO_0000011 | POA | Population Origins or Ancestry Research Only | Boolean | | User must describe research use in IDU statement |
| DUO_0000044 | NPOA | Population Origins or Ancestry Research Prohibited | Boolean |  | Agree to terms |
| DUO_0000027 | PS | Project Specific Restriction | Boolean |  | User prompted to provide IDU statement |
| DUO_0000024 | MOR | Publication Moratorium | String |  Provide date [ISO 8601] | Agree to terms |
| DUO_0000019 | PUB | Publication Required | Boolean | | Agree to terms |
| DUO_0000012 | RS | Research Specific Restrictions | String | Provide detail | User must describe research use in IDU statement |
| DUO_0000029 | RTN | Return to Database or Resource | Boolean | | Agree to terms |
| DUO_0000025 | TS | Time Limit on Use | String | Provide date [ISO 8601] | User prompted to renew access every _x_ days |
| DUO_0000026 | US | User Specific Restriction | String | Provide detail | User may be required to join a Synapse Team or have a specific authentication, e.g., 2FA or RAS
|  | DUOplus1 | Source Geography | List of Strings | List data generating country(ies) [ISO 3166⍺2] | 
|  | DUOplus2 | Study Size | Integer | "n" | 
|  | DUOplus3 | Deidentifcation | List of Strings | Method for de-identification | 
|  | DUOplus4 | Data Permission | List of Strings | Data sharing enforced by: Agreement, Attestation, Award, Other (TBD) |
|  | DUOplus5 | Data Tier | List of Strings | Anonymous, Open (aka Registered), Controlled, Private |
|  | DUOplus6 | License | List of Strings | CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA |
|  | DUOplus7 | Attribution | String | Provide attribution/acknowledgement statement |
