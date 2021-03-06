# -*- coding: utf-8 -*-
import scipy
import scipy.io as sio
import numpy as np
import pandas as pd


def loadmat(filename):
    """
    this function should be called instead of direct spio.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    """

    def _check_keys(d):
        """
        checks if entries in dictionary are mat-objects. If yes
        todict is called to change them to nested dictionaries
        """
        for key in d:
            if isinstance(d[key], sio.matlab.mio5_params.mat_struct):
                d[key] = _todict(d[key])
        return d

    def _has_struct(elem):
        """Determine if elem is an array and if any array item is a struct"""
        return isinstance(elem, np.ndarray) and any(
            isinstance(e, scipy.io.matlab.mio5_params.mat_struct) for e in elem
        )

    def _todict(matobj):
        """
        A recursive function which constructs from matobjects nested dictionaries
        """
        d = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, sio.matlab.mio5_params.mat_struct):
                d[strg] = _todict(elem)
            elif _has_struct(elem):
                d[strg] = _tolist(elem)
            else:
                d[strg] = elem
        return d

    def _tolist(ndarray):
        """
        A recursive function which constructs lists from cellarrays
        (which are loaded as numpy ndarrays), recursing into the elements
        if they contain matobjects.
        """
        elem_list = []
        for sub_elem in ndarray:
            if isinstance(sub_elem, sio.matlab.mio5_params.mat_struct):
                elem_list.append(_todict(sub_elem))
            elif _has_struct(sub_elem):
                elem_list.append(_tolist(sub_elem))
            else:
                elem_list.append(sub_elem)
        return elem_list

    data = scipy.io.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)


def get_khodayari_kos():
    return {
        "fbaA": "result_cont_Delta_fbaAB.mat",
        "fbaB": "result_cont_Delta_fbaAB.mat",
        "fbp": "result_cont_Delta_fbp.mat",
        "gnd": "result_cont_Delta_gnd.mat",
        "pfkA": "result_cont_Delta_pfkAB.mat",
        "pfkB": "result_cont_Delta_pfkAB.mat",
        "pgi": "result_cont_Delta_pgi.mat",
        "pgl": "result_cont_Delta_pgl.mat",
        "ppsA": "result_cont_Delta_ppsA.mat",
        # "pts": "result_cont_Delta_pts.mat",
        "pykA": "result_cont_Delta_pykA.mat",
        "pykF": "result_cont_Delta_pykF.mat",
        "rpe": "result_cont_Delta_rpe.mat",
        "rpiA": "result_cont_Delta_rpiAB.mat",
        "rpiB": "result_cont_Delta_rpiAB.mat",
        # "sdhCD": "result_cont_Delta_sdhCD.mat",
        "sucA": "result_cont_Delta_sucAB.mat",
        "talA": "result_cont_Delta_talAB.mat",
        "tktA": "result_cont_Delta_tktAB.mat",
        "tktB": "result_cont_Delta_tktAB.mat",
        "tpi": "result_cont_Delta_tpi.mat",
        "zwf": "result_cont_Delta_zwf.mat",
        "WT": "result_cont_WT.mat",
    }


def get_khodayari_batch_kos():
    return {
        "fbaA": "result_cont_Delta_fbaAB.mat",
        "fbaB": "result_cont_Delta_fbaAB.mat",
        "fbp": "result_cont_Delta_fbp.mat",
        "gnd": "result_cont_Delta_gnd.mat",
        "pfkA": "result_cont_Delta_pfkAB.mat",
        "pfkB": "result_cont_Delta_pfkAB.mat",
        "pgi": "result_cont_Delta_pgi.mat",
        "pgl": "result_cont_Delta_pgl.mat",
        "ppsA": "result_cont_Delta_ppsA.mat",
        # "pts": "result_cont_Delta_pts.mat",
        "pykA": "result_cont_Delta_pykA.mat",
        "pykF": "result_cont_Delta_pykF.mat",
        "rpe": "result_cont_Delta_rpe.mat",
        "rpiA": "result_cont_Delta_rpiAB.mat",
        "rpiB": "result_cont_Delta_rpiAB.mat",
        # "sdhCD": "result_cont_Delta_sdhCD.mat",
        "sucA": "result_cont_Delta_sucAB.mat",
        "talA": "result_cont_Delta_talAB.mat",
        "tktA": "result_cont_Delta_tktAB.mat",
        "tktB": "result_cont_Delta_tktAB.mat",
        "tpi": "result_cont_Delta_tpi.mat",
        "zwf": "result_cont_Delta_zwf.mat",
        "WT": "result_cont_WT.mat",
        "eda": "result_cont_Delta_eda.mat",
        "edd": "result_cont_Delta_edd.mat",
    }


def get_millard_kos():
    return {
        # "fbaA": "Millard_result_Delta_fba.csv",
        # "fbaB": "Millard_result_Delta_fba.csv",
        "fbp": "Millard_result_Delta_fbp.csv",
        "gnd": "Millard_result_Delta_gnd.csv",
        # "pfkA": "Millard_result_Delta_pfk.csv",
        # "pfkB": "Millard_result_Delta_pfk.csv",
        "pgi": "Millard_result_Delta_pgi.csv",
        "pgl": "Millard_result_Delta_pgl.csv",
        "ppsA": "Millard_result_Delta_pps.csv",
        # "pts": "Millard_result_Delta_pts.csv",
        "pykA": "Millard_result_Delta_pyk.csv",
        "pykF": "Millard_result_Delta_pyk.csv",
        "rpe": "Millard_result_Delta_rpe.csv",
        "rpiA": "Millard_result_Delta_rpi.csv",
        "rpiB": "Millard_result_Delta_rpi.csv",
        "sdhCD": "Millard_result_Delta_sdh.csv",
        "talAB": "Millard_result_Delta_tal.csv",
        "tktA": "Millard_result_Delta_tkt1.csv",
        # "tkt2": "Millard_result_Delta_tkt2.csv",
        # "tpi": "Millard_result_Delta_tpi.csv",
        "zwf": "Millard_result_Delta_zwf.csv",
        # "sucA": "Millard_result_Delta_aAkgdh.csv",
        "WT": "Millard_result_WT.csv",
    }


def get_millard_batch_kos():
    return {
        # "fbaA": "Millard_result_Delta_fba.csv",
        # "fbaB": "Millard_result_Delta_fba.csv",
        "fbp": "Millard_result_Delta_fbp.csv",
        "gnd": "Millard_result_Delta_gnd.csv",
        # "pfkA": "Millard_result_Delta_pfk.csv",
        # "pfkB": "Millard_result_Delta_pfk.csv",
        "pgi": "Millard_result_Delta_pgi.csv",
        "pgl": "Millard_result_Delta_pgl.csv",
        "ppsA": "Millard_result_Delta_pps.csv",
        # "pts": "Millard_result_Delta_pts.csv",
        "pykA": "Millard_result_Delta_pyk.csv",
        "pykF": "Millard_result_Delta_pyk.csv",
        "rpe": "Millard_result_Delta_rpe.csv",
        "rpiA": "Millard_result_Delta_rpi.csv",
        "rpiB": "Millard_result_Delta_rpi.csv",
        "sdhCD": "Millard_result_Delta_sdh.csv",
        "talAB": "Millard_result_Delta_tal.csv",
        "tktA": "Millard_result_Delta_tkt1.csv",
        # "tkt2": "Millard_result_Delta_tkt2.csv",
        # "tpi": "Millard_result_Delta_tpi.csv",
        "zwf": "Millard_result_Delta_zwf.csv",
        # "sucA": "Millard_result_Delta_aAkgdh.csv",
        "WT": "Millard_result_WT.csv",
        "eda": "Millard_result_Delta_eda.csv",
        "edd": "Millard_result_Delta_edd.csv",
    }


def get_kurata_kos():
    return {
        "fbaA": "result_cont_Delta_fbaB.mat",
        "fbaB": "result_cont_Delta_fbaB.mat",
        "fbp": "result_cont_Delta_fbp.mat",
        "gnd": "result_cont_Delta_gnd.mat",
        # "gpmA": "result_cont_Delta_gpmA.mat",
        "pfkA": "result_cont_Delta_pfkA.mat",
        "pfkB": "result_cont_Delta_pfkB.mat",
        "pgi": "result_cont_Delta_pgi.mat",
        "ppc": "result_cont_Delta_ppc.mat",
        # "pgl": "result_cont_Delta_pgl.mat",
        "ppsA": "result_cont_Delta_ppsA.mat",
        "pts": "result_cont_Delta_pts.mat",
        "pykA": "result_cont_Delta_pykA.mat",
        "pykF": "result_cont_Delta_pykF.mat",
        # "rpe": "result_cont_Delta_rpe.mat",
        "rpiA": "result_cont_Delta_rpiA.mat",
        "rpiB": "result_cont_Delta_rpiB.mat",
        "sdhCD": "result_cont_Delta_sdhC.mat",
        "sucA": "result_cont_Delta_sucAC.mat",
        "talA": "result_cont_Delta_talA.mat",
        "talB": "result_cont_Delta_talB.mat",
        "tktA": "result_cont_Delta_tktA.mat",
        "tktB": "result_cont_Delta_tktB.mat",
        "tpi": "result_cont_Delta_tpi.mat",
        "zwf": "result_cont_Delta_zwf.mat",
        "glk": "result_cont_Delta_glk.mat",
        "WT": "result_cont_WT.mat",
    }


def get_kurata_batch_kos():
    return {
        "fbaA": "result_batch_Delta_fbaB.mat",
        # "fbaB": "result_batch_Delta_fbaB.mat",
        "fbp": "result_batch_Delta_fbp.mat",
        "gnd": "result_batch_Delta_gnd.mat",
        # "gpmA": "result_batch_Delta_gpmA.mat",
        "pfkA": "result_batch_Delta_pfkA.mat",
        "pfkB": "result_batch_Delta_pfkB.mat",
        "pgi": "result_batch_Delta_pgi.mat",
        "ppc": "result_batch_Delta_ppc.mat",
        # "pgl": "result_batch_Delta_pgl.mat",
        "ppsA": "result_batch_Delta_ppsA.mat",
        "pts": "result_batch_Delta_pts.mat",
        "pykA": "result_batch_Delta_pykA.mat",
        "pykF": "result_batch_Delta_pykF.mat",
        # "rpe": "result_batch_Delta_rpe.mat",
        "rpiA": "result_batch_Delta_rpiA.mat",
        "rpiB": "result_batch_Delta_rpiB.mat",
        "sdhCD": "result_batch_Delta_sdhC.mat",
        "sucA": "result_batch_Delta_sucAC.mat",
        "talA": "result_batch_Delta_talA.mat",
        "talB": "result_batch_Delta_talB.mat",
        "tktA": "result_batch_Delta_tktA.mat",
        "tktB": "result_batch_Delta_tktB.mat",
        "tpi": "result_batch_Delta_tpi.mat",
        "zwf": "result_batch_Delta_zwf.mat",
        "glk": "result_batch_Delta_glk.mat",
        "eda": "result_batch_Delta_eda.mat",
        "edd": "result_batch_Delta_edd.mat",
        "WT" : "result_batch_RF06.mat",
    }


def get_kotte_kos():
    return {
        "fbaAB": "Kotte_result_Delta_fba.csv",
        "fbp": "Kotte_result_Delta_fbp.csv",
        "pfkA": "Kotte_result_Delta_pfk.csv",
        "ppsA": "Kotte_result_Delta_pps.csv",
        "pts": "Kotte_result_Delta_pts.csv",
        "pykF": "Kotte_result_Delta_pyk.csv",
    }


def get_chassagnole_kos():
    return {
        "fbaA": "Chassagnole_result_Delta_fba.csv",
        "fbaB": "Chassagnole_result_Delta_fba.csv",
        "gnd": "Chassagnole_result_Delta_gnd.csv",
        "pfkA": "Chassagnole_result_Delta_pfk.csv",
        "pfkB": "Chassagnole_result_Delta_pfk.csv",
        "pgi": "Chassagnole_result_Delta_pgi.csv",
        # "pts": "Chassagnole_result_Delta_pts.csv",
        "pykA": "Chassagnole_result_Delta_pyk.csv",
        "pykF": "Chassagnole_result_Delta_pyk.csv",
        "rpe": "Chassagnole_result_Delta_rpe.csv",
        "rpiA": "Chassagnole_result_Delta_rpi.csv",
        "rpiB": "Chassagnole_result_Delta_rpi.csv",
        "talA": "Chassagnole_result_Delta_tal.csv",
        "talB": "Chassagnole_result_Delta_tal.csv",
        "tkt1": "Chassagnole_result_Delta_tkt1.csv",
        "tkt2": "Chassagnole_result_Delta_tkt2.csv",
        "tpi": "Chassagnole_result_Delta_tpi.csv",
        "zwf": "Chassagnole_result_Delta_zwf.csv",
        "WT": "Chassagnole_result_WT.csv",
    }


def get_khodayari_zwf():
    samples = ["dzwf", "WT", "zwf(15)"]
    return {k: f"khodayari_zwf_sens_{k}.mat" for k in samples}


def get_kurata_zwf():
    samples = ["dzwf", "WT", "zwf(15)"]
    return {k: f"kurata_zwf_sens_{k}.mat" for k in samples}


def get_millard_zwf():
    samples = ["dzwf", "WT", "zwf(15)"]
    return {k: f"millard_zwf_sens_{k}.csv" for k in samples}


def get_khodayari_pgi():
    samples = ["dpgi", "pgi(0)", "pgi(20)", "pgi(50)", "pgi(100)", "WT"]
    return {k: f"khodayari_pgi_sens_{k}.mat" for k in samples}


def get_kurata_pgi():
    samples = ["dpgi", "pgi(0)", "pgi(20)", "pgi(50)", "pgi(100)", "WT"]
    return {k: f"kurata_pgi_sens_{k}.mat" for k in samples}


def get_millard_pgi():
    samples = ["dpgi", "pgi(0)", "pgi(20)", "pgi(50)", "pgi(100)", "WT"]
    return {k: f"millard_pgi_sens_{k}.csv" for k in samples}


def get_khodayari_eno():
    samples = ["eno(0)", "eno(50)", "eno(200)", "eno(500)", "WT"]
    return {k: f"khodayari_eno_sens_{k}.mat" for k in samples}


def get_kurata_eno():
    samples = ["eno(0)", "eno(50)", "eno(200)", "eno(500)", "WT"]
    return {k: f"kurata_eno_sens_{k}.mat" for k in samples}


def get_millard_eno():
    samples = ["eno(0)", "eno(50)", "eno(200)", "eno(500)", "WT"]
    return {k: f"millard_eno_sens_{k}.csv" for k in samples}


def get_chassagnole_zwf():
    samples = ["dzwf", "zwf(15)"]
    files = {k: f"chassagnole_{k}.csv" for k in samples}
    files["WT"] = "chassagnole_sens_WT.csv"
    return files


def get_chassagnole_pgi():
    samples = ["dpgi", "pgi(0)", "pgi(20)", "pgi(50)", "pgi(100)"]
    files = {k: f"chassagnole_{k}.csv" for k in samples}
    files["WT"] = "chassagnole_sens_WT.csv"
    return files


def get_chassagnole_eno():
    samples = ["eno(0)", "eno(50)", "eno(200)", "eno(500)"]
    files = {k: f"chassagnole_{k}.csv" for k in samples}
    files["WT"] = "chassagnole_sens_WT.csv"
    return files


def get_kurata_dilutions():
    samples = ["0.2", "0.4", "0.6", "0.7"]
    return {k: f"kurata_dilution_{k.replace('.','')}.mat" for k in samples}


def get_khodayari_dilutions():
    samples = ["0.2", "0.4", "0.6", "0.7"]
    return {k: f"khodayari_dilution_{k.replace('.','')}.mat" for k in samples}


def get_millard_dilutions():
    samples = ["0.2", "0.4", "0.6", "0.7"]
    return {k: f"millard_dilution_{k.replace('.','')}.csv" for k in samples}


def get_chassagnole_dilutions():
    samples = ["0.2", "0.4", "0.6", "0.7"]
    return {k: f"Chassagnole_result_{k.replace('.','')}.csv" for k in samples}

# Set of routines to load data for various models
# and present them as pandas dataframe


def load_khodayari(sample_names, load_path, id_df, files=None):
    """ Will return single dataframe with columns:
    - author=Khodayari, 
    - sample_id corresponding to relevant sample
    - flux with correspoding value in original units
    - ID showing original id
    - BiGG ID with BiGG identifier
    params:
    :sample_names - list of sample names or "all"
    :load_path - Path object where the samples are located
    :id_df - pd.DataFrame with conversion Model ID -> BiGG ID
    :files - dict where key is sample name and value is filename
    """

    if files is None:
        raise ValueError("files dictionary is not specified")

    if type(sample_names) is not list:
        sample_names = [sample_names]

    # check mismatch with sample names in inputs
    unknown_ids = [elem for elem in sample_names if elem not in files.keys()]

    if sample_names == ["all"]:
        sample_names = files.keys()
    elif unknown_ids:
        error_msg = ", ".join(unknown_ids)
        raise ValueError(f"Unable to find relevant data for {error_msg}")

    res_df = pd.DataFrame()
    for sample_id in sample_names:
        file_name = files[sample_id]
        data = loadmat(load_path / file_name)
        data_shape = data["Vnet"].shape
        print(
            f"Loaded data file for sample {sample_id} which has flux matrix of {data_shape}"
        )

        # data['Vnet'][:,data_shape[1]-1] is the last column of integration, ideally it should be closer to steady state
        # khod_rxn_ids[455] is the index of 'Biomass' flux, the last flux id
        df = pd.DataFrame(
            {
                "flux": data["Vnet"][0:457, data_shape[1] - 1],
                "ID": id_df["ID"],
                "BiGG_ID": id_df["BiGG ID"],
            }
        )
        df = df.assign(author="Khodayari", sample_id=sample_id)

        # fix PGM direction
        df.loc[df["ID"] == "PGM", "flux"] = (
            -1 * df.loc[df["ID"] == "PGM", "flux"].values[0]
        )

        # fix PGK direction
        df.loc[df["ID"] == "PGK", "flux"] = (
            -1 * df.loc[df["ID"] == "PGK", "flux"].values[0]
        )

        # fix RPI direction
        df.loc[df["ID"] == "RPI", "flux"] = (
            -1 * df.loc[df["ID"] == "RPI", "flux"].values[0]
        )

        # normalize to the glucose uptake
        glucose_uptake = df[df["ID"] == "EX_glc(e)"]["flux"].values[0]
        df = df.assign(normalized_flux=lambda x: x.flux * 100 / glucose_uptake)

        # update
        res_df = pd.concat([res_df, df])

    return res_df


def load_kurata(sample_names, load_path, id_df, files=None, mode="continuous"):
    """ Will return single dataframe with columns:
    - author=Kurata, 
    - sample_id corresponding to relevant sample
    - flux with correspoding value in original units
    - ID with BiGG identifier
    params:
    :sample_names - list of sample names or "all"
    :load_path - Path object where the samples are located
    :id_df - pd.DataFrame with conversion Model ID -> BiGG ID
    :files - dict where key is sample name and value is filename
      """
    if files is None:
        raise ValueError("files dictionary is not specified")

    if type(sample_names) is not list:
        sample_names = [sample_names]

    # check mismatch with sample names in inputs
    unknown_ids = [elem for elem in sample_names if elem not in files.keys()]

    if sample_names == ["all"]:
        sample_names = files.keys()
    elif unknown_ids:
        error_msg = ", ".join(unknown_ids)
        raise ValueError(f"Unable to find relevant data for {error_msg}")

    res_df = pd.DataFrame()
    for sample_id in sample_names:
        file_name = files[sample_id]
        data = loadmat(load_path / file_name)
        data_shape = data["FLUX"].shape
        print(
            f"Loaded data file for sample {sample_id} which has flux matrix of {data_shape}"
        )

        # this weird construction helps to deal with multiple IDs corresponding to Gapdh reaction
        # which in Kuratas model is a sum of gapA, tpiA, gpmA or gpmM, eno, pgk
        # resulting id would be GAPD.
        kurata_ids = id_df[["ID", "BiGG ID"]].drop_duplicates(subset="ID")

        if mode == "continuous":
            flux_index = 2100
        elif mode == "batch":
            # 5 hour sampling time for batch
            flux_index = 101 + 10 * 5

        df = pd.DataFrame(
            {
                "flux": data["FLUX"][flux_index,],
                "ID": kurata_ids["ID"].values,
                "BiGG_ID": kurata_ids["BiGG ID"].values,
            }
        )
        df = df.assign(author="Kurata", sample_id=sample_id)

        # add results from Gapdh reaction
        flux_val = df[df["BiGG_ID"] == "GAPD"]["flux"].values[0]
        add_fluxes_df = pd.DataFrame(
            {
                "flux": flux_val,
                "ID": "Gapdh",
                "BiGG_ID": ["TPI", "PGM", "ENO", "PGK"],
                "author": "Kurata",
                "sample_id": sample_id,
            }
        )
        df = df.append(add_fluxes_df, sort=False)

        # calculate normalized fluxes with respect to Glucose consumption
        glucose_uptake = (
            df[df["ID"] == "vPts4"]["flux"].values[0]
            + df[df["ID"] == "vNonpts"]["flux"].values[0]
        )
        df = df.assign(normalized_flux=lambda x: x.flux * 100 / glucose_uptake)

        # update
        res_df = pd.concat([res_df, df])

    return res_df


def load_millard(sample_names, load_path, id_df, files=None):
    """ Will return single dataframe with columns:
    - author=Millard, 
    - sample_id corresponding to relevant sample
    - flux with correspoding value in original units
    - ID with BiGG identifier
    params:
    :sample_names - list of sample names or "all"
    :load_path - Path object where the samples are located
    :id_df - pd.DataFrame with conversion Model ID -> BiGG ID
    :files - dict where key is sample name and value is filename
      """
    if files is None:
        raise ValueError("files dictionary is not specified")

    if type(sample_names) is not list:
        sample_names = [sample_names]

    # check mismatch with sample names in inputs
    unknown_ids = [elem for elem in sample_names if elem not in files.keys()]

    if sample_names == ["all"]:
        sample_names = files.keys()
    elif unknown_ids:
        error_msg = ", ".join(unknown_ids)
        raise ValueError(f"Unable to find relevant data for {error_msg}")

    res_df = pd.DataFrame()
    for sample_id in sample_names:
        file_name = files[sample_id]

        data = pd.read_csv(load_path / file_name)
        data_shape = data["ID"].shape
        print(
            f"Loaded data file for sample {sample_id} which has flux matrix of {data_shape}"
        )

        df = pd.merge(
            left=data.drop("Unnamed: 0", axis=1),
            right=id_df[["ID", "BiGG ID"]],
            how="left",
            on="ID",
        )

        df = df.assign(author="Millard", sample_id=sample_id)
        df = df.rename({"BiGG ID": "BiGG_ID", "Value": "flux"}, axis=1)

        # Set MDH reaction to be the difference between MQO and MDH flux
        mdh_flux = (
            df.loc[df.ID == "MQO", "flux"].values[0]
            - df.loc[df.ID == "MDH", "flux"].values[0]
        )
        df.loc[df.BiGG_ID == "MDH", "flux"] = mdh_flux

        # Calculate normalized fluxes
        glucose_uptake = df[df["ID"] == "XCH_GLC"]["flux"].values[0]
        df = df.assign(normalized_flux=lambda x: x.flux * 100 / glucose_uptake)

        # update
        res_df = pd.concat([res_df, df])

    return res_df


def load_kotte(sample_names, load_path, id_df, files=None):

    """ Will return single dataframe with columns:
    - author=Millard, 
    - sample_id corresponding to relevant sample
    - flux with correspoding value in original units
    - ID with BiGG identifier
    params:
    :sample_names - list of sample names or "all"
    :load_path - Path object where the samples are located
    :id_df - pd.DataFrame with conversion Model ID -> BiGG ID
    :files - dict where key is sample name and value is filename
      """
    if files is None:
        raise ValueError("files dictionary is not specified")

    if type(sample_names) is not list:
        sample_names = [sample_names]

    # check mismatch with sample names in inputs
    unknown_ids = [elem for elem in sample_names if elem not in files.keys()]

    if sample_names == ["all"]:
        sample_names = files.keys()
    elif unknown_ids:
        error_msg = ", ".join(unknown_ids)
        raise ValueError(f"Unable to find relevant data for {error_msg}")

    res_df = pd.DataFrame()
    for sample_id in sample_names:
        file_name = files[sample_id]

        data = pd.read_csv(load_path / file_name)
        data_shape = data["ID"].shape
        print(
            f"Loaded data file for sample {sample_id} which has flux matrix of {data_shape}"
        )

        df = pd.merge(
            left=data.drop("Unnamed: 0", axis=1),
            right=id_df[["ID", "BiGG ID"]],
            how="left",
            on="ID",
        )

        df = df.assign(author="Kotte", sample_id=sample_id)
        df = df.rename({"BiGG ID": "BiGG_ID", "Value": "flux"}, axis=1)
        # update
        res_df = pd.concat([res_df, df])

    return res_df


def load_chassagnole(sample_names, load_path, id_df, files=None):
    """ Will return single dataframe with columns:
    - author=Chassagnole, 
    - sample_id corresponding to relevant sample
    - flux with correspoding value in original units
    - ID with BiGG identifier
    params:
    :sample_names - list of sample names or "all"
    :load_path - Path object where the samples are located
    :id_df - pd.DataFrame with conversion Model ID -> BiGG ID
    :files - dict where key is sample name and value is filename
      """
    if files is None:
        raise ValueError("files dictionary is not specified")

    if type(sample_names) is not list:
        sample_names = [sample_names]

    # check mismatch with sample names in inputs
    unknown_ids = [elem for elem in sample_names if elem not in files.keys()]

    if sample_names == ["all"]:
        sample_names = files.keys()
    elif unknown_ids:
        error_msg = ", ".join(unknown_ids)
        raise ValueError(f"Unable to find relevant data for {error_msg}")

    res_df = pd.DataFrame()
    for sample_id in sample_names:
        file_name = files[sample_id]

        data = pd.read_csv(load_path / file_name)
        data_shape = data["ID"].shape
        print(
            f"Loaded data file for sample {sample_id} which has flux matrix of {data_shape}"
        )

        df = pd.merge(
            left=data.drop("Unnamed: 0", axis=1),
            right=id_df[["ID", "BiGG ID"]],
            how="left",
            on="ID",
        )

        df = df.assign(author="Chassagnole", sample_id=sample_id)
        df = df.rename({"BiGG ID": "BiGG_ID", "Value": "flux"}, axis=1)

        # Calculate normalized fluxes
        glucose_uptake = df[df["ID"] == "vPTS"]["flux"].values[0]
        df = df.assign(normalized_flux=lambda x: x.flux * 100 / glucose_uptake)

        # update
        res_df = pd.concat([res_df, df])

    return res_df
