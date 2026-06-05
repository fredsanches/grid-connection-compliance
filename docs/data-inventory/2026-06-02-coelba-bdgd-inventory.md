# BDGD Inventory

- **Source:** ANEEL BDGD open data portal
- **Download date:** 2026-06-01
- **GDB path:** `data\raw\bdgd\coelba\Neoenergia_Coelba_47_2024-12-31_V11_20250902-0855.gdb`

## Minimum Feeder Topology Candidates

| Concept | Candidate Layer(s) | Candidate Columns | Confidence | Notes |
|---|---|---|---|---|
| Substation | SUB | COD_ID, NOME | High | Candidate feeder source boundary; Validated against BDGD manual.|
| Low-voltage consumer load source | UCBT_tab | UNI_TR_MT, CTMT, UNI_TR_AT, SUB, TEN_FORN, SIT_ATIV, CAR_INST, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12 | Medium | Lower-voltage consumer units. `ENE_01` to `ENE_12` are monthly active energy in kWh; useful for load estimation, but conversion from monthly energy to OpenDSS kW/kvar still requires an aggregation/load-shape rule. |
| Medium-voltage consumer load source | UCMT_tab | UNI_TR_MT, CTMT, UNI_TR_AT, SUB, TEN_FORN, SIT_ATIV, CAR_INST, DEM_CONT, ENE_01, DEM_01, DEM_02, DEM_03, DEM_04, DEM_05, DEM_06, DEM_07, DEM_08, DEM_09, DEM_10, DEM_11, DEM_12 ,ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12 | Medium | Medium-voltage consumer units. `DEM_01` to `DEM_12` represent demand by period and `ENE_01` to `ENE_12` represent active energy by period; useful for base-case load estimation, but OpenDSS conversion still requires validating demand units, period definition, reactive power/power factor assumptions, and the electrical connection mapping. |
| High-voltage consumer load source | UCAT_tab | COD_ID, CTAT, SUB, CEG_GD, FAS_CON, TEN_FORN, SIT_ATIV, CAR_INST, DEM_CONT, DEM_P_01, DEM_P_02, DEM_P_03, DEM_P_04, DEM_P_05, DEM_P_06, DEM_P_07, DEM_P_08, DEM_P_09, DEM_P_10, DEM_P_11, DEM_P_12, DEM_F_01, DEM_F_02, DEM_F_03, DEM_F_04, DEM_F_05, DEM_F_06, DEM_F_07, DEM_F_08, DEM_F_09, DEM_F_10, DEM_F_11, DEM_F_12, ENE_P_01, ENE_P_02, ENE_P_03, ENE_P_04, ENE_P_05, ENE_P_06, ENE_P_07, ENE_P_08, ENE_P_09, ENE_P_10, ENE_P_11, ENE_P_12, ENE_F_01, ENE_F_02, ENE_F_03, ENE_F_04, ENE_F_05, ENE_F_06, ENE_F_07, ENE_F_08, ENE_F_09, ENE_F_10, ENE_F_11, ENE_F_12 | Medium | High-voltage consumer units. `DEM_P_01` to `DEM_P_12` represent max active peak demand by period, `DEM_F_01` to `DEM_F_12` represent max active off-peak demand by period, `ENE_P_01` to `ENE_P_12` represent active peak energy by period and; `ENE_F_01` to `ENE_F_12` represent active off-peak energy by period; OpenDSS conversion still requires validating demand units, period definition, reactive power/power factor assumptions, and the electrical connection mapping. |
| Low-voltage generation unit | UGBT_tab | COD_ID, CEG_GD, UNI_TR_MT, CTMT, UNI_TR_AT, SUB, TEN_CON, SIT_ATIV, POT_INST, DEM_CONT, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12 | Medium | Low-voltage distributed generation units. `POT_INST` is a candidate installed capacity field and `ENE_01` to `ENE_12` are period energy fields; useful for existing DG representation, but OpenDSS conversion requires validating generation type, capacity units, energy sign convention, dispatch/profile assumptions, and transformer connection through `UNI_TR_MT`. |
| Medium-voltage generation unit | UGMT_tab | COD_ID, CEG_GD, CTMT, UNI_TR_AT, SUB, TEN_CON, SIT_ATIV, POT_INST, DEM_CONT, DEM_01, DEM_02, DEM_03, DEM_04, DEM_05, DEM_06, DEM_07, DEM_08, DEM_09, DEM_10, DEM_11, DEM_12, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12 | Medium | Medium-voltage distributed generation units. Candidate source for existing DG connected directly to the MV feeder; requires validating capacity units, energy fields, operating profile, and bus/PAC connection before creating OpenDSS generator objects. |
| High-voltage generation unit | UGAT_tab | COD_ID, CTAT, CEG_GD, SUB, TEN_CON, SIT_ATIV, POT_INST, DEM_CONT, TIP_SIST, DEM_P_01, DEM_P_02, DEM_P_03, DEM_P_04, DEM_P_05, DEM_P_06, DEM_P_07, DEM_P_08, DEM_P_09, DEM_P_10, DEM_P_11, DEM_P_12, DEM_F_01, DEM_F_02, DEM_F_03, DEM_F_04, DEM_F_05, DEM_F_06, DEM_F_07, DEM_F_08, DEM_F_09, DEM_F_10, DEM_F_11, DEM_F_12, ENE_P_01, ENE_P_02, ENE_P_03, ENE_P_04, ENE_P_05, ENE_P_06, ENE_P_07, ENE_P_08, ENE_P_09, ENE_P_10, ENE_P_11, ENE_P_12, ENE_F_01, ENE_F_02, ENE_F_03, ENE_F_04, ENE_F_05, ENE_F_06, ENE_F_07, ENE_F_08, ENE_F_09, ENE_F_10, ENE_F_11, ENE_F_12 | Medium | High-voltage distributed generation units. Candidate source for existing DG connected directly to the HV feeder; requires validating capacity units, energy fields, operating profile, and bus/PAC connection before creating OpenDSS generator objects. |
| Pole/support point | PONNOT | COD_ID, TIP_PN, TIP_INST | Low | Utility Pole/support-point layer with physical construction attributes such as installation type, structure type, material, and height. It does not directly reference line segments; any relationship must be resolved from segment layers that carry `PN_CON_1` and `PN_CON_2`. Useful for validating physical endpoint/support metadata and later contesting pole/structure upgrade claims, but not directly required for OpenDSS steady-state power flow unless segment pole references need enrichment. |
| Lower-voltage line segment | SSDBT | COD_ID, PN_CON_1, PN_CON_2, UNI_TR_MT, CTMT, CT_COD_OP, UNI_TR_AT, SUB, FAS_CON, PAC_1, PAC_2, TIP_INST, TIP_CND, COMP | Medium | `PAC_1` and `PAC_2` are candidate electrical endpoints, `PN_CON_1` and `PN_CON_2` may reference physical pole/support points from `PONNOT`, `TIP_CND` is the candidate conductor reference, `FAS_CON` indicates connected phases, and `COMP` is the candidate segment length. |
| Medium-voltage line segment | SSDMT | COD_ID, PN_CON_1, PN_CON_2, CTMT, CT_COD_OP, UNI_TR_AT, SUB, PAC_1, PAC_2, FAS_CON, TIP_INST, TIP_CND, COMP | Medium | `PAC_1` and `PAC_2` are candidate electrical endpoints, `PN_CON_1` and `PN_CON_2` may reference physical pole/support points from `PONNOT`, `TIP_CND` is the candidate conductor reference, `FAS_CON` indicates connected phases, and `COMP` is the candidate segment length. |
| High-voltage line segment | SSDAT | COD_ID, PN_CON_1, PN_CON_2, CTAT, CT_COD_OP, PAC_1, PAC_2, FAS_CON, TIP_INST, TIP_CND, COMP | Medium | `PAC_1` and `PAC_2` are candidate electrical endpoints, `PN_CON_1` and `PN_CON_2` may reference physical pole/support points from `PONNOT`, `TIP_CND` is the candidate conductor reference, `FAS_CON` indicates connected phases, and `COMP` is the candidate segment length. |
| Low-voltage reactive compensation unit | UNCRBT | COD_ID, FAS_CON, SIT_ATIV, POT_NOM, PAC_1, PAC_2, UNI_TR_MT, CTMT, UNI_TR_AT, SUB, BANC | Low | Layer exists in the BDGD schema but has `row_count = 0` in the Coelba dataset. No low-voltage reactive compensation units are available for this snapshot, so this layer is not required for the current parser slice. Keep as a future-supported asset type. `BANC` is flag to indicate if this object is a equipment bank (0=False, 1=True). Check if this is relevant in future. |
| Medium-voltage reactive compensation unit | UNCRMT | COD_ID, FAS_CON, SIT_ATIV, POT_NOM, PAC_1, PAC_2, CTMT, UNI_TR_AT, SUB, BANC | Medium | Medium-voltage reactive compensation units connected to the feeder. `POT_NOM` is the candidate nominal reactive power rating, `FAS_CON` indicates connected phases, `SIT_ATIV` indicates operating/asset status, `PAC_1` and `PAC_2` are candidate electrical connection points, and `BANC` may identify capacitor bank grouping. Important for voltage profile, reactive power flow, and PRODIST Módulo 8 compliance; validate whether the unit behaves as fixed, switched, or controlled compensation before mapping to OpenDSS capacitor/reactor objects. |
| High-voltage reactive compensation unit | UNCRAT | COD_ID, FAS_CON, SIT_ATIV, POT_NOM, PAC_1, PAC_2, SUB, BANC | Medium | High-voltage reactive compensation units connected to the feeder. `POT_NOM` is the candidate nominal reactive power rating, `FAS_CON` indicates connected phases, `SIT_ATIV` indicates operating/asset status, `PAC_1` and `PAC_2` are candidate electrical connection points, and `BANC` may identify capacitor bank grouping. Important for voltage profile, reactive power flow, and PRODIST Módulo 8 compliance; validate whether the unit behaves as fixed, switched, or controlled compensation before mapping to OpenDSS capacitor/reactor objects. |
| Medium-voltage regulation unit | UNREMT | COD_ID, FAS_CON, SIT_ATIV, PAC_1, PAC_2, CTMT, UNI_TR_AT, SUB, BANC | Medium | Medium-voltage regulation units connected to the feeder. `FAS_CON` indicates connected phases, `SIT_ATIV` indicates operating/asset status, `PAC_1` and `PAC_2` are candidate electrical connection points, and `BANC` may identify capacitor bank grouping. Important for voltage profile, power flow, and PRODIST Módulo 8 compliance; validate whether the unit behaves as validate regulator type (`TIP_REGU`), control behavior, voltage regulation settings from `EQRE`, active status, phases, and terminal mapping before creating OpenDSS RegControl/Transformer objects. |
| High-voltage regulation unit | UNREAT | COD_ID, FAS_CON, SIT_ATIV, PAC_1, PAC_2, SUB, BANC | Medium | High-voltage regulation units connected to the feeder. `FAS_CON` indicates connected phases, `SIT_ATIV` indicates operating/asset status, `PAC_1` and `PAC_2` are candidate electrical connection points, and `BANC` may identify capacitor bank grouping. Important for voltage profile, power flow, and PRODIST Módulo 8 compliance; validate whether the unit behaves as validate regulator type (`TIP_REGU`), control behavior, voltage regulation settings from `EQRE`, active status, phases, and terminal mapping before creating OpenDSS RegControl/Transformer objects. |
| Low-voltage disconnect switch | UNSEBT | COD_ID, PAC_1, PAC_2, FAS_CON, SIT_ATIV, P_N_OPE, CAP_ELO, COR_NOM, UNI_TR_MT, CTMT, UNI_TR_AT, SUB | Medium | Low-voltage disconnect/protection switching device. `PAC_1` and `PAC_2` are candidate electrical terminals, `FAS_CON` indicates connected phases, `SIT_ATIV` indicates asset status, `P_N_OPE` references the normal operating position, `CAP_ELO` references fuse/link current capacity, and `COR_NOM` is nominal current. Relevant for LV topology reconstruction and protection-state validation; not required for the first MV feeder model unless LV network switching, transformer secondary behavior, or consumer/generation connection tracing is in scope. |
| Medium-voltage disconnect switch | UNSEMT | COD_ID, PAC_1, PAC_2, FAS_CON, SIT_ATIV, P_N_OPE, CAP_ELO, COR_NOM, CTMT, UNI_TR_AT, SUB | Medium | Medium-voltage disconnect/protection switching device. `PAC_1` and `PAC_2` are candidate electrical terminals, `FAS_CON` indicates connected phases, `SIT_ATIV` indicates asset status, `P_N_OPE` references the normal operating position, `CAP_ELO` references fuse/link current capacity, and `COR_NOM` is nominal current. |
| High-voltage disconnect switch | UNSEAT | COD_ID, PAC_1, PAC_2, FAS_CON, SIT_ATIV, P_N_OPE, CAP_ELO, COR_NOM, SUB | Medium | High-voltage disconnect/protection switching device. `PAC_1` and `PAC_2` are candidate electrical terminals, `FAS_CON` indicates connected phases, `SIT_ATIV` indicates asset status, `P_N_OPE` references the normal operating position, `CAP_ELO` references fuse/link current capacity, and `COR_NOM` is nominal current. |
| High-voltage transformer unit | UNTRAT | COD_ID, SUB, BARR_1, BARR_2, BARR_3, PAC_1, PAC_2, PAC_3, FAS_CON_P, FAS_CON_S, FAS_CON_T, SIT_ATIV, POT_NOM, POT_F01, POT_F02, PER_TOT, BANC, TIP_TRAFO, ENES_01, ENES_02, ENES_03, ENES_04, ENES_05, ENES_06, ENES_07, ENES_08, ENES_09, ENES_10, ENES_11, ENES_12, ENET_01, ENET_02, ENET_03, ENET_04, ENET_05, ENET_06, ENET_07, ENET_08, ENET_09, ENET_10, ENET_11, ENET_12, ENES_01_IN, ENES_02_IN, ENES_03_IN, ENES_04_IN, ENES_05_IN, ENES_06_IN, ENES_07_IN, ENES_08_IN, ENES_09_IN, ENES_10_IN, ENES_11_IN, ENES_12_IN, ENET_01_IN, ENET_02_IN, ENET_03_IN, ENET_04_IN, ENET_05_IN, ENET_06_IN, ENET_07_IN, ENET_08_IN, ENET_09_IN, ENET_10_IN, ENET_11_IN, ENET_12_IN | Medium | High-voltage transformer unit associated with substation/source boundary modeling. `POT_NOM` defines nominal apparent power, `POT_F01` and `POT_F02` indicate forced-ventilation ratings, `PER_FER` and `PER_TOT` describe loss percentages, `PAC_*` and `BARR_*` are candidate electrical terminal/busbar references, and `ENES_*`/`ENET_*` plus inverse-flow variants provide energy evidence by winding and period. Useful for source transformer capacity and reverse-flow analysis, but OpenDSS conversion still requires validating voltage bases, winding configuration, impedance assumptions, and linked busbar records. Coelba field names use `_IN` for inverse-flow transformer energy fields, while the manual excerpt describes `_INV`; parser mapping must use observed Coelba column names and document this schema variation. |
| Medium-voltage transformer unit | UNTRMT | COD_ID, PAC_1, PAC_2, PAC_3, FAS_CON_P, FAS_CON_S, FAS_CON_T, SIT_ATIV, TEN_LIN_SE, CAP_ELO, CAP_CHA, TAP, CONF, POSTO, POT_NOM, PER_FER, PER_TOT, CTMT, UNI_TR_AT, SUB, BANC, TIP_TRAFO, MRT | High | Medium-voltage distribution transformer units. Core layer for linking MV feeder topology to downstream LV loads and generation. `PAC_1` and `PAC_2` are candidate electrical terminals, `CTMT` links the transformer to the MV feeder, `UNI_TR_AT` and `SUB` link it to the upstream source context, `POT_NOM` gives nominal apparent power in kVA, `TEN_LIN_SE` gives secondary line voltage in kV, `TAP` gives secondary voltage adjustment in p.u., and `PER_FER`/`PER_TOT` provide loss data in watts. Required for OpenDSS transformer modeling, but primary voltage and complete winding assumptions must be validated from feeder/source metadata before conversion. |
| Accessant service connection branch | RAMLIG | COD_ID, PN_CON_1, PN_CON_2, PAC_1, PAC_2, UNI_TR_MT, CTMT, FAS_CON, UNI_TR_AT, SUB, TIP_INST, TIP_CND, COMP | Medium | Service connection branch for an accessant. `PAC_1` and `PAC_2` are candidate electrical terminals, `PN_CON_1` and `PN_CON_2` reference physical support points from `PONNOT`, `UNI_TR_MT`, `CTMT`, `UNI_TR_AT`, and `SUB` locate the branch in the transformer/feeder/source hierarchy, `FAS_CON` indicates connected phases, `TIP_CND` references conductor type through `SEGCON`, and `COMP` gives branch length in meters. Useful for tracing consumer/generator interconnections and contesting local service-branch upgrades; not a primary MV feeder backbone layer. |
| Medium-voltage circuit/feeders | CTMT | COD_ID, NOME, BARR, SUB, PAC_INI, TEN_NOM, TEN_OPE, ATIP, RECONFIG, UNI_TR_AT, ENE_01...ENE_12, PERD_A3a, PERD_A4, PERD_B, PERD_MED, PERD_A3aA4, PERD_A3a_B, PERD_A4A3a, PERD_A4_B, PERD_B_A3a, PERD_B_A4, PNTMT_01...PNTMT_12, PNTBT_01...PNTBT_12 | High | Medium-voltage feeder/circuit definition. `COD_ID` identifies the feeder, `BARR` and `SUB` link it to the source busbar/substation, `PAC_INI` is the candidate initial electrical coupling point, `TEN_NOM` references nominal line voltage through `TTEN`, `TEN_OPE` gives operating voltage in p.u., and `UNI_TR_AT` links the feeder to the high-voltage transformer unit when present. Core source-boundary layer for feeder topology and OpenDSS voltage-base setup; energy and loss fields are useful for later load/loss validation and contestation analysis. |
| High-voltage circuit | CTAT | COD_ID, NOME, TEN_NOM, PAC_INI | Medium | High-voltage circuit definition. Useful for upstream/source context and potential substation-boundary modeling, but not required for the first MV feeder topology parser unless the study explicitly includes AT network constraints. `TEN_NOM` references nominal line voltage through `TTEN`, and `PAC_INI` is the candidate initial electrical coupling point. |
| Substation busbar | BAR | COD_ID, SUB, TIP_INST, TEN_NOM, PAC, POS, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC | High | Substation busbar layer related to `UNTRAT` and `CTMT`. `COD_ID` is referenced by `CTMT.BARR` and `UNTRAT.BARR_*`, `SUB` links the busbar to the substation, `TEN_NOM` references nominal busbar voltage through `TTEN`, and `PAC` gives the electrical coupling point. Core source-boundary layer for feeder voltage-base setup; patrimonial and ownership fields are useful later for contesting substation/busbar upgrade scope. |
| Conductor segment type | SEGCON | COD_ID, GEOM_CAB, FORM_CAB, BIT_FAS_1, BIT_FAS_2, BIT_FAS_3, BIT_NEU, MAT_FAS_1, MAT_FAS_2, MAT_FAS_3, MAT_NEU, ISO_FAS_1, ISO_FAS_2, ISO_FAS_3, ISO_NEU, CND_FAS, R1, X1, R_REGUL, FTRCNV, CNOM, CMAX | High | Conductor segment reference table used by line/branch layers through `TIP_CND`. `R1` and `X1` provide positive-sequence impedance in ohms/km, `CNOM` and `CMAX` provide nominal and maximum conductor current limits in amperes, and conductor material/bitola/insulation fields support ampacity and upgrade-scope validation. Critical for OpenDSS line-code creation, voltage-drop/rise studies, thermal loading checks, and contesting unnecessary reconductoring. |

## Reference Tables Required for Topology Slice

| Reference Table | Used By | Required Fields | Priority | Notes |
|---|---|---|---|---|
| TTEN | BAR.TEN_NOM, CTMT.TEN_NOM, CTAT.TEN_NOM | COD_ID, TEN | High | Voltage-code reference table. Required to convert nominal voltage references into actual kV values for OpenDSS voltage-base setup. Must be loaded before converting busbars, feeders, or source circuits into simulation objects. |
| TCABOBIT | SEGCON.BIT_FAS_1, SEGCON.BIT_FAS_2, SEGCON.BIT_FAS_3, SEGCON.BIT_NEU | COD_ID, DESCR | Medium | Conductor gauge/bitola reference table. Useful for validating conductor physical type and contesting reconductoring assumptions. Not required for first OpenDSS line-code creation if `R1`, `X1`, `CNOM`, and `CMAX` are present. |
| TCABOMAT | SEGCON.MAT_FAS_1, SEGCON.MAT_FAS_2, SEGCON.MAT_FAS_3, SEGCON.MAT_NEU | COD_ID, DESCR | Medium | Conductor material reference table. Useful for validating ampacity assumptions and utility upgrade scope. |
| TCABOISO | SEGCON.ISO_FAS_1, SEGCON.ISO_FAS_2, SEGCON.ISO_FAS_3, SEGCON.ISO_NEU | COD_ID, DESCR | Medium | Conductor insulation reference table. Useful for physical conductor characterization and upgrade-scope validation. |
| TCABOGEOM | SEGCON.GEOM_CAB | COD_ID, DESCR | Low | Cable geometry reference table. Useful for conductor characterization; not required for first positive-sequence approximation. |
| TCABOFOR | SEGCON.FORM_CAB | COD_ID, DESCR | Low | Cable formation reference table. Useful for conductor characterization; not required for first positive-sequence approximation. |
| TRESREGUL | SEGCON.R_REGUL | COD_ID, RES_REGUL, DESCR | Medium | Regulatory resistance reference table. Useful for checking whether reported conductor resistance aligns with regulatory reference values. |
| TFASCON | FAS_CON, FAS_CON_P, FAS_CON_S, FAS_CON_T | COD_ID, QUANT_FIOS, FASES, DESCR | High | Phase-connection reference table. Required to translate BDGD phase codes into OpenDSS phases for lines, transformers, switches, regulators, compensation units, loads, and generation. |
| TSITATI | SIT_ATIV | COD_ID, DESCR | High | Asset activation/status reference table. Required to filter active/inactive equipment before building feeder topology. |
| TUNI | TIP_UNID | COD_ID, UNIDADE, TIPO_UNIDADE | Medium | Unit-type reference table. Useful for distinguishing equipment unit configurations before OpenDSS conversion. |
| TCAPELFU | CAP_ELO | COD_ID, DESCR | Medium | Fuse/link capacity reference table. Useful for protection and switching-device limits, especially for upgrade-scope contestation. |
| TCOR | COR_NOM, CAP_CHA | COD_ID, CORR, DESCR | Medium | Current-capacity reference table. Used by nominal switch current and switch capacity fields. Useful for protection/thermal limit validation. |
| TTRANF | TIP_TRAFO | COD_ID, DESCR | Medium | Transformer-type reference table. Useful for classifying transformer construction before OpenDSS conversion. |
| TCONFIG | UNTRMT.CONF | COD_ID, DESCR | Medium | Transformer circuit-configuration reference table. Required if `CONF` affects winding or phase interpretation. |
| TPOSTOTRAN | UNTRMT.POSTO | COD_ID, DESCR | Low | Transformer installation/post reference table. Useful for documentation and contestation, not first topology. |
| TINST | TIP_INST | COD_ID, DESCR | Low | Installation-type reference table. Useful for asset characterization and upgrade-scope evidence. |
| TPOS | POS | COD_ID, DESCR | Low | Ownership/possession reference table. Useful for contestation evidence, not power-flow topology. |

Note: These reference/code tables were identified from the BDGD manual. They were not listed as layers in the Coelba `.gdb` inventory output, so the parser must verify whether they are available from another BDGD source, embedded domain metadata, or must be modeled as external lookup dictionaries.

## Equipment Detail Tables Required for Electrical Modeling

| Detail Table | Used By | Required Fields | Priority | Notes |
|---|---|---|---|---|
| EQTRMT | UNTRMT.COD_ID / EQTRMT.UNI_TR_MT | UNI_TR_MT, TEN_PRI, TEN_SEC, TEN_TER, LIG, FAS_CON, LIG_FAS_P, LIG_FAS_S, LIG_FAS_T, R, XHL, XHT, XLT, PER_FER, PER_TOT | High | Medium-voltage transformer equipment detail table. `UNTRMT` provides transformer location/topology, while `EQTRMT` provides primary/secondary/tertiary voltages, winding/phase connection data, resistance, reactance, and loss fields required for OpenDSS transformer modeling. Required before converting `UNTRMT` records into simulation-ready transformer objects. |
| EQTRAT | UNTRAT.COD_ID / EQTRAT.UNI_TR_AT | UNI_TR_AT, TEN_PRI, TEN_SEC, TEN_TER, LIG, FAS_CON, POT_NOM, PER_FER, PER_TOT, POT_F01, POT_F02 | Medium | High-voltage transformer equipment detail table. Useful for source transformer and substation-boundary modeling. |
| EQSE | UNSEBT, UNSEMT, UNSEAT | UN_SE, FAS_CON, COR_NOM, ELO_FSV, ABER_CRG, CLAS_TEN | Medium | Switch/protection equipment detail table. Useful for validating switching device ratings and open/closed/load-break behavior. |
| EQRE | UNREMT, UNREAT | UN_RE, POT_NOM, TEN_REG, LIG_FAS_P, LIG_FAS_S, COR_NOM, R, XHL, PER_FER, PER_TOT | Medium | Regulator equipment detail table. Important for voltage-regulation modeling and PRODIST voltage compliance. |
| EQCR | UNCRBT, UNCRMT, UNCRAT | UN_CR, TIP_INST, GRU_TEN | Medium | Reactive compensation equipment detail table. Useful for classifying compensation equipment; validate whether additional kvar/control data is already in `UNCR*` or needs detail-table resolution. |

## Deferred Supporting Layers

| Layer | Meaning | Priority | Notes |
|---|---|---|---|
| BASE | Distributor/base metadata | Low | Cadastral layer for distributor/base identification. Not required for feeder topology or OpenDSS conversion. |
| PIP | Public lighting point | Low | Public lighting load source. Defer until LV/public-lighting load modeling is included. |
| BE | Energy balance | Low | Aggregate energy-balance information. Useful later for validation, not topology construction. |
| EP | Pass-through energy | Low | Energy-flow reporting layer. Useful later for energy reconciliation, not first parser slice. |
| PT | Technical losses | Medium | Reported technical-loss layer. Useful later to compare OpenDSS-calculated losses against BDGD/utility reported losses. |
| PNT | Non-technical losses | Low | Non-technical-loss layer. Relevant for regulatory/accounting context, but not electrical topology or power-flow modeling. |
| CRVCRG | Load curve | Medium | Load-curve layer related to UC/UG/PIP entities. Not needed for topology, but important later for realistic demand/generation profiles and scenario modeling. |

## Layers

### SSDAT

- Geometry type: `MultiLineString`
- Row count: `59017`
- Candidate concepts: `medium_voltage_segment, conductor`
- Columns: `COD_ID, PN_CON_1, PN_CON_2, CTAT, CT_COD_OP, CONJ, ARE_LOC, DIST, PAC_1, PAC_2, FAS_CON, TIP_INST, TIP_CND, POS, ODI, TI, CM, SITCONT, COMP, DESCR, Shape_Length`

### SSDBT

- Geometry type: `MultiLineString`
- Row count: `2857409`
- Candidate concepts: `medium_voltage_segment, feeder, substation, conductor`
- Columns: `COD_ID, PN_CON_1, PN_CON_2, UNI_TR_MT, CTMT, CT_COD_OP, UNI_TR_AT, SUB, CONJ, ARE_LOC, FAS_CON, DIST, PAC_1, PAC_2, TIP_INST, TIP_CND, POS, ODI, TI, CM, SITCONT, COMP, DESCR, Shape_Length`

### SSDMT

- Geometry type: `MultiLineString`
- Row count: `3244930`
- Candidate concepts: `medium_voltage_segment, feeder, substation, conductor`
- Columns: `COD_ID, PN_CON_1, PN_CON_2, CTMT, CT_COD_OP, UNI_TR_AT, SUB, CONJ, ARE_LOC, DIST, PAC_1, PAC_2, FAS_CON, TIP_INST, TIP_CND, POS, ODI, TI, CM, SITCONT, COMP, DESCR, Shape_Length`

### PONNOT

- Geometry type: `Point`
- Row count: `5011213`
- Candidate concepts: `load, distributed_generation`
- Columns: `COD_ID, DIST, TIP_PN, TIP_INST, POS, ESTR, MAT, ESF, ALT, ARE_LOC, CONJ, MUN, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, SITCONT, DESCR`

### UNCRAT

- Geometry type: `Point`
- Row count: `5`
- Candidate concepts: `medium_voltage_segment, substation, transformer`
- Columns: `COD_ID, DIST, FAS_CON, SIT_ATIV, TIP_UNID, POT_NOM, PAC_1, PAC_2, SUB, CONJ, MUN, ARE_LOC, DAT_CON, BANC, POS, DESCR`

### UNCRBT

- Geometry type: `Point`
- Row count: `0`
- Candidate concepts: `medium_voltage_segment, feeder, substation, transformer`
- Columns: `COD_ID, DIST, FAS_CON, SIT_ATIV, TIP_UNID, POT_NOM, PAC_1, PAC_2, UNI_TR_MT, CTMT, UNI_TR_AT, SUB, CONJ, MUN, ARE_LOC, DAT_CON, BANC, POS, DESCR`

### UNCRMT

- Geometry type: `Point`
- Row count: `1394`
- Candidate concepts: `medium_voltage_segment, feeder, substation, transformer`
- Columns: `COD_ID, DIST, FAS_CON, SIT_ATIV, TIP_UNID, POT_NOM, PAC_1, PAC_2, CTMT, UNI_TR_AT, SUB, CONJ, MUN, ARE_LOC, DAT_CON, BANC, POS, DESCR`

### UNREAT

- Geometry type: `Point`
- Row count: `8`
- Candidate concepts: `medium_voltage_segment, substation`
- Columns: `COD_ID, DIST, FAS_CON, SIT_ATIV, TIP_UNID, TIP_REGU, PAC_1, PAC_2, SUB, CONJ, MUN, DAT_CON, BANC, POS, DESCR`

### UNREMT

- Geometry type: `Point`
- Row count: `1183`
- Candidate concepts: `medium_voltage_segment, feeder, substation`
- Columns: `COD_ID, DIST, FAS_CON, SIT_ATIV, TIP_UNID, TIP_REGU, PAC_1, PAC_2, CTMT, UNI_TR_AT, SUB, CONJ, MUN, DAT_CON, BANC, POS, DESCR`

### UNSEAT

- Geometry type: `Point`
- Row count: `4244`
- Candidate concepts: `medium_voltage_segment, substation`
- Columns: `COD_ID, DIST, PAC_1, PAC_2, FAS_CON, SIT_ATIV, TIP_UNID, P_N_OPE, CAP_ELO, COR_NOM, TLCD, DAT_CON, SUB, CONJ, MUN, POS, DESCR`

### UNSEBT

- Geometry type: `Point`
- Row count: `0`
- Candidate concepts: `medium_voltage_segment, feeder, substation`
- Columns: `COD_ID, DIST, PAC_1, PAC_2, FAS_CON, SIT_ATIV, TIP_UNID, P_N_OPE, CAP_ELO, COR_NOM, TLCD, DAT_CON, POS, UNI_TR_MT, CTMT, UNI_TR_AT, SUB, CONJ, MUN, ARE_LOC, DESCR`

### UNSEMT

- Geometry type: `Point`
- Row count: `253088`
- Candidate concepts: `medium_voltage_segment, feeder, substation`
- Columns: `COD_ID, DIST, PAC_1, PAC_2, FAS_CON, SIT_ATIV, TIP_UNID, P_N_OPE, CAP_ELO, COR_NOM, TLCD, DAT_CON, POS, CTMT, UNI_TR_AT, SUB, CONJ, MUN, ARE_LOC, DESCR`

### UNTRAT

- Geometry type: `Point`
- Row count: `444`
- Candidate concepts: `medium_voltage_segment, substation, transformer`
- Columns: `COD_ID, SUB, BARR_1, BARR_2, BARR_3, PAC_1, PAC_2, PAC_3, DIST, FAS_CON_P, FAS_CON_S, FAS_CON_T, SIT_ATIV, TIP_UNID, POS, ARE_LOC, POT_NOM, POT_F01, POT_F02, PER_FER, PER_TOT, BANC, DAT_CON, CONJ, MUN, TIP_TRAFO, ALOC_PERD, ENES_01, ENES_02, ENES_03, ENES_04, ENES_05, ENES_06, ENES_07, ENES_08, ENES_09, ENES_10, ENES_11, ENES_12, ENET_01, ENET_02, ENET_03, ENET_04, ENET_05, ENET_06, ENET_07, ENET_08, ENET_09, ENET_10, ENET_11, ENET_12, ENES_01_IN, ENES_02_IN, ENES_03_IN, ENES_04_IN, ENES_05_IN, ENES_06_IN, ENES_07_IN, ENES_08_IN, ENES_09_IN, ENES_10_IN, ENES_11_IN, ENES_12_IN, ENET_01_IN, ENET_02_IN, ENET_03_IN, ENET_04_IN, ENET_05_IN, ENET_06_IN, ENET_07_IN, ENET_08_IN, ENET_09_IN, ENET_10_IN, ENET_11_IN, ENET_12_IN, DESCR`

### UNTRMT

- Geometry type: `Point`
- Row count: `375105`
- Candidate concepts: `medium_voltage_segment, feeder, substation, transformer`
- Columns: `COD_ID, DIST, PAC_1, PAC_2, PAC_3, FAS_CON_P, FAS_CON_S, FAS_CON_T, SIT_ATIV, TIP_UNID, POS, ATRB_PER, TEN_LIN_SE, CAP_ELO, CAP_CHA, TAP, ARE_LOC, CONF, POSTO, POT_NOM, PER_FER, PER_TOT, DAT_CON, CTMT, UNI_TR_AT, SUB, CONJ, MUN, BANC, TIP_TRAFO, MRT, DESCR`

### ARAT

- Geometry type: `MultiPolygon`
- Row count: `1`
- Candidate concepts: `none`
- Columns: `COD_ID, DIST, FUN_PR, FUN_TE, DESCR, Shape_Length, Shape_Area`

### CONJ

- Geometry type: `MultiPolygon`
- Row count: `211`
- Candidate concepts: `substation`
- Columns: `COD_ID, DIST, NOME, SIST_INTE, SIST_SUBT, DESCR, Shape_Length, Shape_Area`

### SUB

- Geometry type: `MultiPolygon`
- Row count: `638`
- Candidate concepts: `substation`
- Columns: `COD_ID, DIST, POS, NOME, DESCR, Shape_Length, Shape_Area`

### BAR

- Geometry type: `None`
- Row count: `918`
- Candidate concepts: `substation, load, distributed_generation`
- Columns: `COD_ID, SUB, DIST, TIP_INST, TEN_NOM, POS, PAC, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC, SITCONT, DAT_IMO, DESCR`

### BASE

- Geometry type: `None`
- Row count: `1`
- Candidate concepts: `none`
- Columns: `DIST, DAT_INC, DAT_FNL, DAT_EXT, DESCR`

### BAY

- Geometry type: `None`
- Row count: `2586`
- Candidate concepts: `substation`
- Columns: `COD_ID, DIST, SUB_GRP, POS, SUB, TIP_BAY, DESCR`

### BE

- Geometry type: `None`
- Row count: `27`
- Candidate concepts: `substation`
- Columns: `COD_ID, DIST, SUB_GRP, ORG_ENER, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DESCR`

### CRVCRG

- Geometry type: `None`
- Row count: `312`
- Candidate concepts: `none`
- Columns: `COD_ID, DIST, TIP_DIA, POT_01, POT_02, POT_03, POT_04, POT_05, POT_06, POT_07, POT_08, POT_09, POT_10, POT_11, POT_12, POT_13, POT_14, POT_15, POT_16, POT_17, POT_18, POT_19, POT_20, POT_21, POT_22, POT_23, POT_24, POT_25, POT_26, POT_27, POT_28, POT_29, POT_30, POT_31, POT_32, POT_33, POT_34, POT_35, POT_36, POT_37, POT_38, POT_39, POT_40, POT_41, POT_42, POT_43, POT_44, POT_45, POT_46, POT_47, POT_48, POT_49, POT_50, POT_51, POT_52, POT_53, POT_54, POT_55, POT_56, POT_57, POT_58, POT_59, POT_60, POT_61, POT_62, POT_63, POT_64, POT_65, POT_66, POT_67, POT_68, POT_69, POT_70, POT_71, POT_72, POT_73, POT_74, POT_75, POT_76, POT_77, POT_78, POT_79, POT_80, POT_81, POT_82, POT_83, POT_84, POT_85, POT_86, POT_87, POT_88, POT_89, POT_90, POT_91, POT_92, POT_93, POT_94, POT_95, POT_96, GRU_TEN, DESCR`

### CTAT

- Geometry type: `None`
- Row count: `543`
- Candidate concepts: `none`
- Columns: `COD_ID, NOME, TEN_NOM, PAC_INI, DIST, DESCR`

### CTMT

- Geometry type: `None`
- Row count: `1486`
- Candidate concepts: `feeder, substation`
- Columns: `COD_ID, NOME, BARR, SUB, PAC_INI, TEN_NOM, TEN_OPE, ATIP, RECONFIG, DIST, UNI_TR_AT, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, PERD_A3a, PERD_A4, PERD_B, PERD_MED, PERD_A3aA4, PERD_A3a_B, PERD_A4A3a, PERD_A4_B, PERD_B_A3a, PERD_B_A4, PNTMT_01, PNTMT_02, PNTMT_03, PNTMT_04, PNTMT_05, PNTMT_06, PNTMT_07, PNTMT_08, PNTMT_09, PNTMT_10, PNTMT_11, PNTMT_12, PNTBT_01, PNTBT_02, PNTBT_03, PNTBT_04, PNTBT_05, PNTBT_06, PNTBT_07, PNTBT_08, PNTBT_09, PNTBT_10, PNTBT_11, PNTBT_12, DESCR`

### EP

- Geometry type: `None`
- Row count: `11`
- Candidate concepts: `substation`
- Columns: `COD_ID, DIST, SUB_GRP_PR, SUB_GRP_SE, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DESCR`

### EQCR

- Geometry type: `None`
- Row count: `1537`
- Candidate concepts: `load, distributed_generation`
- Columns: `COD_ID, DIST, TIP_INST, UN_CR, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC, SITCONT, DAT_IMO, GRU_TEN, DESCR`

### EQME

- Geometry type: `None`
- Row count: `6819196`
- Candidate concepts: `load, distributed_generation`
- Columns: `COD_ID, PAC, DIST, TIP_INST, TIP_UNID, FAS_CON, TIPMED, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, SITCONT, DAT_IMO, GRU_TEN, DESCR, UC_UG`

### EQRE

- Geometry type: `None`
- Row count: `3354`
- Candidate concepts: `transformer, switch_or_recloser, load, distributed_generation`
- Columns: `COD_ID, DIST, TIP_INST, UN_RE, POT_NOM, TEN_REG, LIG_FAS_P, LIG_FAS_S, COR_NOM, REL_TP, REL_TC, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC, SITCONT, DAT_IMO, PER_FER, PER_TOT, R, XHL, GRU_TEN, DESCR`

### EQSE

- Geometry type: `None`
- Row count: `687145`
- Candidate concepts: `load, distributed_generation`
- Columns: `COD_ID, DIST, TIP_INST, UN_SE, CLAS_TEN, ELO_FSV, MEI_ISO, FAS_CON, COR_NOM, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC, SITCONT, DAT_IMO, ABER_CRG, GRU_TEN, DESCR`

### EQTRAT

- Geometry type: `None`
- Row count: `444`
- Candidate concepts: `transformer, load, distributed_generation`
- Columns: `COD_ID, DIST, TIP_INST, UNI_TR_AT, CLAS_TEN, POT_NOM, LIG, FAS_CON, TEN_PRI, TEN_SEC, TEN_TER, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC, SITCONT, DAT_IMO, PER_FER, PER_TOT, POT_F01, POT_F02, DESCR`

### EQTRM

- Geometry type: `None`
- Row count: `24755`
- Candidate concepts: `substation, load, distributed_generation`
- Columns: `COD_ID, SUB, DIST, PAC, TIP_INST, TIP_UNID, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC, SITCONT, DAT_IMO, GRU_TEN, DESCR, UC_UG`

### EQTRMT

- Geometry type: `None`
- Row count: `375108`
- Candidate concepts: `transformer, load, distributed_generation`
- Columns: `COD_ID, DIST, TIP_INST, UNI_TR_MT, CLAS_TEN, POT_NOM, LIG, FAS_CON, TEN_PRI, TEN_SEC, TEN_TER, LIG_FAS_P, LIG_FAS_S, LIG_FAS_T, ODI, TI, CM, TUC, A1, A2, A3, A4, A5, A6, UAR, IDUC, SITCONT, DAT_IMO, PER_FER, PER_TOT, R, XHL, XHT, XLT, DESCR`

### PIP

- Geometry type: `None`
- Row count: `1556743`
- Candidate concepts: `feeder, substation, switch_or_recloser, load, distributed_generation`
- Columns: `COD_ID, UC_ID, DIST, MUN, CONJ, SUB, UNI_TR_AT, CTMT, UNI_TR_MT, PN_CON, CLAS_SUB, FAS_CON, GRU_TEN, TEN_FORN, GRU_TAR, SIT_ATIV, ARE_LOC, PAC, TIP_CC, CAR_INST, TIPO_LAMP, POT_LAMP, PERDA_REAT, PERDA_RELE, PERDA_OUTR, CONTROLE, TIP_SIST, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DIC, FIC, LIV, SEMRED, DAT_CON, DESCR`

### PNT

- Geometry type: `None`
- Row count: `3`
- Candidate concepts: `substation`
- Columns: `COD_ID, DIST, SUB_GRP, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DESCR`

### PT

- Geometry type: `None`
- Row count: `17`
- Candidate concepts: `none`
- Columns: `COD_ID, DIST, CATEG, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DESCR`

### RAMLIG

- Geometry type: `None`
- Row count: `6877831`
- Candidate concepts: `medium_voltage_segment, feeder, substation, conductor`
- Columns: `COD_ID, PN_CON_1, PN_CON_2, DIST, PAC_1, PAC_2, UNI_TR_MT, CTMT, FAS_CON, UNI_TR_AT, SUB, CONJ, ARE_LOC, TIP_INST, TIP_CND, POS, ODI, TI, CM, SITCONT, COMP, DESCR`

### SEGCON

- Geometry type: `None`
- Row count: `1188`
- Candidate concepts: `conductor, load, distributed_generation`
- Columns: `COD_ID, DIST, GEOM_CAB, FORM_CAB, BIT_FAS_1, BIT_FAS_2, BIT_FAS_3, BIT_NEU, MAT_FAS_1, MAT_FAS_2, MAT_FAS_3, MAT_NEU, ISO_FAS_1, ISO_FAS_2, ISO_FAS_3, ISO_NEU, CND_FAS, R1, X1, R_REGUL, FTRCNV, CNOM, CMAX, TUC_FAS, A1_FAS, A2_FAS, A3_FAS, A4_FAS, A5_FAS, A6_FAS, TUC_NEU, A1_NEU, A2_NEU, A3_NEU, A4_NEU, A5_NEU, A6_NEU, UAR, DESCR`

### UCAT_tab

- Geometry type: `None`
- Row count: `99`
- Candidate concepts: `substation, load, distributed_generation`
- Columns: `PN_CON, DIST, PAC, CTAT, SUB, CONJ, MUN, CEG_GD, BRR, CEP, CLAS_SUB, CNAE, TIP_CC, FAS_CON, GRU_TEN, TEN_FORN, GRU_TAR, SIT_ATIV, DAT_CON, CAR_INST, DEM_CONT, LIV, ARE_LOC, TIP_SIST, DEM_P_01, DEM_P_02, DEM_P_03, DEM_P_04, DEM_P_05, DEM_P_06, DEM_P_07, DEM_P_08, DEM_P_09, DEM_P_10, DEM_P_11, DEM_P_12, DEM_F_01, DEM_F_02, DEM_F_03, DEM_F_04, DEM_F_05, DEM_F_06, DEM_F_07, DEM_F_08, DEM_F_09, DEM_F_10, DEM_F_11, DEM_F_12, ENE_P_01, ENE_P_02, ENE_P_03, ENE_P_04, ENE_P_05, ENE_P_06, ENE_P_07, ENE_P_08, ENE_P_09, ENE_P_10, ENE_P_11, ENE_P_12, ENE_F_01, ENE_F_02, ENE_F_03, ENE_F_04, ENE_F_05, ENE_F_06, ENE_F_07, ENE_F_08, ENE_F_09, ENE_F_10, ENE_F_11, ENE_F_12, DIC_01, DIC_02, DIC_03, DIC_04, DIC_05, DIC_06, DIC_07, DIC_08, DIC_09, DIC_10, DIC_11, DIC_12, FIC_01, FIC_02, FIC_03, FIC_04, FIC_05, FIC_06, FIC_07, FIC_08, FIC_09, FIC_10, FIC_11, FIC_12, DESCR, COD_ID`

### UCBT_tab

- Geometry type: `None`
- Row count: `7307231`
- Candidate concepts: `feeder, substation, load, distributed_generation`
- Columns: `DIST, PAC, RAMAL, PN_CON, UNI_TR_MT, CTMT, UNI_TR_AT, SUB, CONJ, MUN, CEG_GD, BRR, CEP, CLAS_SUB, CNAE, TIP_CC, FAS_CON, GRU_TEN, TEN_FORN, GRU_TAR, SIT_ATIV, DAT_CON, CAR_INST, LIV, ARE_LOC, TIP_SIST, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DIC_01, DIC_02, DIC_03, DIC_04, DIC_05, DIC_06, DIC_07, DIC_08, DIC_09, DIC_10, DIC_11, DIC_12, FIC_01, FIC_02, FIC_03, FIC_04, FIC_05, FIC_06, FIC_07, FIC_08, FIC_09, FIC_10, FIC_11, FIC_12, SEMRED, DESCR, COD_ID`

### UCMT_tab

- Geometry type: `None`
- Row count: `23015`
- Candidate concepts: `feeder, substation, load, distributed_generation`
- Columns: `PN_CON, DIST, PAC, CTMT, UNI_TR_AT, SUB, CONJ, MUN, CEG_GD, BRR, CEP, CLAS_SUB, CNAE, TIP_CC, FAS_CON, GRU_TEN, TEN_FORN, GRU_TAR, SIT_ATIV, DAT_CON, CAR_INST, DEM_CONT, LIV, ARE_LOC, TIP_SIST, DEM_01, DEM_02, DEM_03, DEM_04, DEM_05, DEM_06, DEM_07, DEM_08, DEM_09, DEM_10, DEM_11, DEM_12, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DIC_01, DIC_02, DIC_03, DIC_04, DIC_05, DIC_06, DIC_07, DIC_08, DIC_09, DIC_10, DIC_11, DIC_12, FIC_01, FIC_02, FIC_03, FIC_04, FIC_05, FIC_06, FIC_07, FIC_08, FIC_09, FIC_10, FIC_11, FIC_12, SEMRED, DESCR, COD_ID`

### UGAT_tab

- Geometry type: `None`
- Row count: `54`
- Candidate concepts: `substation`
- Columns: `PN_CON, DIST, PAC, CTAT, CEG_GD, CONJ, MUN, SUB, BRR, CEP, CNAE, FAS_CON, GRU_TEN, TEN_CON, SIT_ATIV, DAT_CON, POT_INST, DEM_CONT, TIP_SIST, DEM_P_01, DEM_P_02, DEM_P_03, DEM_P_04, DEM_P_05, DEM_P_06, DEM_P_07, DEM_P_08, DEM_P_09, DEM_P_10, DEM_P_11, DEM_P_12, DEM_F_01, DEM_F_02, DEM_F_03, DEM_F_04, DEM_F_05, DEM_F_06, DEM_F_07, DEM_F_08, DEM_F_09, DEM_F_10, DEM_F_11, DEM_F_12, ENE_P_01, ENE_P_02, ENE_P_03, ENE_P_04, ENE_P_05, ENE_P_06, ENE_P_07, ENE_P_08, ENE_P_09, ENE_P_10, ENE_P_11, ENE_P_12, ENE_F_01, ENE_F_02, ENE_F_03, ENE_F_04, ENE_F_05, ENE_F_06, ENE_F_07, ENE_F_08, ENE_F_09, ENE_F_10, ENE_F_11, ENE_F_12, DIC_01, DIC_02, DIC_03, DIC_04, DIC_05, DIC_06, DIC_07, DIC_08, DIC_09, DIC_10, DIC_11, DIC_12, FIC_01, FIC_02, FIC_03, FIC_04, FIC_05, FIC_06, FIC_07, FIC_08, FIC_09, FIC_10, FIC_11, FIC_12, DESCR, COD_ID`

### UGBT_tab

- Geometry type: `None`
- Row count: `223606`
- Candidate concepts: `feeder, substation`
- Columns: `PN_CON, DIST, PAC, CEG_GD, UNI_TR_MT, CTMT, UNI_TR_AT, SUB, CONJ, MUN, BRR, CEP, CNAE, FAS_CON, GRU_TEN, TEN_CON, SIT_ATIV, DAT_CON, POT_INST, DEM_CONT, TIP_SIST, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DIC_01, DIC_02, DIC_03, DIC_04, DIC_05, DIC_06, DIC_07, DIC_08, DIC_09, DIC_10, DIC_11, DIC_12, FIC_01, FIC_02, FIC_03, FIC_04, FIC_05, FIC_06, FIC_07, FIC_08, FIC_09, FIC_10, FIC_11, FIC_12, DESCR, COD_ID`

### UGMT_tab

- Geometry type: `None`
- Row count: `3642`
- Candidate concepts: `feeder, substation`
- Columns: `PN_CON, DIST, PAC, CEG_GD, CTMT, UNI_TR_AT, SUB, CONJ, MUN, BRR, CEP, CNAE, FAS_CON, GRU_TEN, TEN_CON, SIT_ATIV, DAT_CON, POT_INST, DEM_CONT, TIP_SIST, DEM_01, DEM_02, DEM_03, DEM_04, DEM_05, DEM_06, DEM_07, DEM_08, DEM_09, DEM_10, DEM_11, DEM_12, ENE_01, ENE_02, ENE_03, ENE_04, ENE_05, ENE_06, ENE_07, ENE_08, ENE_09, ENE_10, ENE_11, ENE_12, DIC_01, DIC_02, DIC_03, DIC_04, DIC_05, DIC_06, DIC_07, DIC_08, DIC_09, DIC_10, DIC_11, DIC_12, FIC_01, FIC_02, FIC_03, FIC_04, FIC_05, FIC_06, FIC_07, FIC_08, FIC_09, FIC_10, FIC_11, FIC_12, DESCR, COD_ID`
