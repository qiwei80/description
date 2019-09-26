# -*- coding: utf-8 -*-
"""Main script."""

import argparse
import json
import os
import six

import tensorflow as tf

from google.protobuf import text_format

from opennmt import __version__
from opennmt.models import catalog
from opennmt.runner import Runner
from opennmt.config import load_model, load_config
from opennmt.utils.misc import classes_in_module
import uuid
import json
import random
import nlp
import normalize
import codecs
import shutil
def _prefix_paths(prefix, paths):
    """Recursively prefix paths.

    Args:
      prefix: The prefix to apply.
      data: A dict of relative paths.

    Returns:
      The updated dict.
    """
    if isinstance(paths, dict):
        for key, path in six.iteritems(paths):
            paths[key] = _prefix_paths(prefix, path)
        return paths
    elif isinstance(paths, list):
        for i, path in enumerate(paths):
            paths[i] = _prefix_paths(prefix, path)
        return paths
    else:
        path = paths
        new_path = os.path.join(prefix, path)
        if tf.gfile.Exists(new_path):
            return new_path
        else:
            return path
def select_end():
    text = ["です","になる","でございます","となります","となる","である","があります","になります","です。","になる。","でございます。","となります。","となる。","である。","があります。","になります。","。"]
    return (text[random.randint(0,len(text)-1)])
def savedata(data_dic,path):
    wf = codecs.open(path+"/test.csv","w",'utf-8')
    f_text = ""
    e_text = ["です","になる","でございます","","","","","",""]
    f_text = data_dic["category1"]
    if data_dic["category2"] in ["トップス","パンツ","アクティブウェア"]:
        f_text = f_text + data_dic["category3"]
    else:
        f_text = f_text + data_dic["category2"]
    text = f_text + "の素材は"
    if len(data_dic["material"]) > 0:
        for m in data_dic["material"]:
            text = text + m +" "
        text = text + select_end()
        wf.write(nlp.splitword2(text))
    text = f_text + "の季節は"
    if len(data_dic["season"]) > 0:
        for s in data_dic["season"]:
            text = text + s+ " "
        text = text +select_end()
        wf.write(nlp.splitword2(text))
    text = f_text +"の袖は"
    if data_dic["sleeve"] != "":
        text = text + data_dic["sleeve"] + select_end()
        wf.write(nlp.splitword2(text))
    text = f_text +"の色は"
    if len(data_dic["color"]) > 0:
        for c in data_dic["color"]:
            text = text + c + " "
        text = text + select_end()
        wf.write(nlp.splitword2(text))
    text = f_text + "のサイズは"
    if data_dic["size"] != "":
        text = text + data_dic["size"] + select_end()
        wf.write(nlp.splitword2(text))
    wf.close()

def create_description(path):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#  parser.add_argument("run", default="infer",help="Run type.")
    parser.add_argument("--config", nargs="+",default=['config/opennmt-defaults.yml', 'config/default.yml'],help="List of configuration files.")
    parser.add_argument("--auto_config", default=False, action="store_true",
                      help="Enable automatic configuration values.")
    parser.add_argument("--model_type", default="",
                      choices=list(classes_in_module(catalog, public_only=True)),
                      help="Model type from the catalog.")
    parser.add_argument("--model", default="",
                      help="Custom model configuration file.")
    parser.add_argument("--run_dir", default="",
                      help="If set, model_dir will be created relative to this location.")
    parser.add_argument("--data_dir", default="",
                      help="If set, data files are expected to be relative to this location.")
    parser.add_argument("--features_file", default=[path+'test.csv'], nargs="+",
                      help="Run inference on this file.")
    parser.add_argument("--predictions_file", default=path+"output.out",
                      help=("File used to save predictions. If not set, predictions are printed "
                            "on the standard output."))
    parser.add_argument("--log_prediction_time", default=False, action="store_true",
                      help="Logs some prediction time metrics.")
    parser.add_argument("--checkpoint_path", default='model/model.ckpt-500000',
                      help=("Checkpoint or directory to use for inference or export "
                            "(when a directory is set, the latest checkpoint is used)."))
    parser.add_argument("--export_dir_base", default=None,
                      help="The base directory of the exported model.")
    parser.add_argument("--num_gpus", type=int, default=1,
                      help="Number of GPUs to use for in-graph replication.")
    parser.add_argument("--chief_host", default="",
                      help="hostname:port of the chief worker (for distributed training).")
    parser.add_argument("--worker_hosts", default="",
                      help=("Comma-separated list of hostname:port of workers "
                            "(for distributed training)."))
    parser.add_argument("--ps_hosts", default="",
                      help=("Comma-separated list of hostname:port of parameter servers "
                            "(for distributed training)."))
    parser.add_argument("--task_type", default="chief",
                      choices=["chief", "worker", "ps", "evaluator"],
                      help="Type of the task to run (for distributed training).")
    parser.add_argument("--task_index", type=int, default=0,
                      help="ID of the task (for distributed training).")
    parser.add_argument("--horovod", default=False, action="store_true",
                      help="Enable Horovod support for this run.")
    parser.add_argument("--log_level", default="INFO",
                      choices=["DEBUG", "ERROR", "FATAL", "INFO", "WARN"],
                      help="Logs verbosity.")
    parser.add_argument("--seed", type=int, default=None,
                      help="Random seed.")
    parser.add_argument("--gpu_allow_growth", default=False, action="store_true",
                      help="Allocate GPU memory dynamically.")
    parser.add_argument("--intra_op_parallelism_threads", type=int, default=0,
                      help=("Number of intra op threads (0 means the system picks "
                            "an appropriate number)."))
    parser.add_argument("--inter_op_parallelism_threads", type=int, default=0,
                      help=("Number of inter op threads (0 means the system picks "
                            "an appropriate number)."))
    parser.add_argument("--session_config", default=None,
                      help=("Path to a file containing a tf.ConfigProto message in text format "
                            "and used to create the TensorFlow sessions."))
    parser.add_argument("--json",default=None,required=True,help=("input data as json string"))
    args = parser.parse_args()
    #inp = args.inputstring
    #print (inp)
    print (args)

    tf.compat.v1.logging.set_verbosity(getattr(tf.compat.v1.logging, args.log_level))

    # Setup cluster if defined.
    if args.chief_host:
        if args.run != "train_and_eval":
            raise ValueError("Distributed training is only supported with the train_and_eval run type")
        os.environ["TF_CONFIG"] = json.dumps({
            "cluster": {
                "chief": [args.chief_host],
                "worker": args.worker_hosts.split(","),
                "ps": args.ps_hosts.split(",")
            },
            "task": {
                "type": args.task_type,
                "index": args.task_index
            }
        })

    # Initialize Horovd if defined.
    if args.horovod:
        import horovod.tensorflow as hvd
        hvd.init()
        is_chief = hvd.rank() == 0
    else:
        hvd = None
        is_chief = args.task_type == "chief"

    # Load and merge run configurations.
    config = load_config(args.config)
    if args.run_dir:
        config["model_dir"] = os.path.join(args.run_dir, config["model_dir"])
    if args.data_dir:
        config["data"] = _prefix_paths(args.data_dir, config["data"])

    if is_chief and not tf.io.gfile.exists(config["model_dir"]):
        tf.logging.info("Creating model directory %s", config["model_dir"])
        tf.gfile.MakeDirs(config["model_dir"])
    model = load_model(
      config["model_dir"],
      model_file=args.model,
      model_name=args.model_type,
      serialize_model=is_chief)
    session_config = tf.compat.v1.ConfigProto(
      intra_op_parallelism_threads=args.intra_op_parallelism_threads,
      inter_op_parallelism_threads=args.inter_op_parallelism_threads)
     # gpu_options=tf.GPUOptions(
     #     allow_growth=args.gpu_allow_growth))
    if args.session_config is not None:
        with open(args.session_config, "rb") as session_config_file:
            text_format.Merge(session_config_file.read(), session_config)
    try:
        data = json.loads(args.json)
        savedata(data,path)
    except:
        print ("json is incorrected")
        exit(1)
    runner = Runner(
      model,
      config,
      seed=args.seed,
      #num_devices=args.num_gpus,
      session_config=session_config,
      auto_config=args.auto_config,
      hvd=hvd)

    if not args.features_file:
        parser.error("--features_file is required for inference.")
    elif len(args.features_file) == 1:
        args.features_file = args.features_file[0]
    print ("begin to run....")
    runner.infer(
        args.features_file,
        predictions_file=args.predictions_file,
        checkpoint_path=args.checkpoint_path,
        log_time=args.log_prediction_time)
    description = normalize.normalize(path+"output.out",data)
    data["description"] = description
    json_str = json.dumps(data,ensure_ascii=False)
	
    return (json_str)

def main():
    dirname = uuid.uuid4().hex
    while os.path.exists("temp/"+dirname):
        dirname = uuid.uuid4().hex
    os.mkdir("temp/"+dirname)
    path = "temp/"+dirname+"/"
    print (create_description(path))
    shutil.rmtree("temp/"+dirname+"/")
    
	
if __name__ == "__main__":
   
    main()
