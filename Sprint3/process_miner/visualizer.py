
from pm4py.objects.log.importer.csv import factory as csv_importer  
from pm4py.objects.log.importer.xes import factory as importer      
from pm4py.objects.conversion.log import factory as conversion_factory
from pm4py.algo.discovery.alpha import factory as alpha_miner
from pm4py.visualization.petrinet import factory as visualizer
from pm4py.util import constants
import global_util
import os


class Pm4pyTools(object):
    def __init__(self, file):
        file_path = None
        if not os.path.abspath(file):
            
            file_path = global_util.get_full_path_input_file(file)
        else:
            file_path = file
        self.fileName = os.path.basename(file_path)

    def get_xes_log(self):
        return

    def get_all_time_(self):
        return

    def get_sorted_time_event(self):
        return

    def filter_log_data(self):
        return



def import_xes_data(filename):
    if not os.path.abspath(filename):
       
        file_path = global_util.get_full_path_input_file(filename)
    else:
        file_path = filename
        filename = os.path.basename(filename)

  
    parameters = {"timestamp_sort": True}
    log = importer.apply(file_path, variant="nonstandard", parameters=parameters)
    print(log)

    
    net, initial_marking, final_marking = alpha_miner.apply(log)

    
    gviz = visualizer.apply(net, initial_marking, final_marking)

    
    file, _ = os.path.splitext(filename)
    output_full_name = "output_" + file + ".png"
    
    output_file = global_util.get_full_path_output_file(output_full_name)

    
    visualizer.save(gviz, output_file)
    
    return output_full_name



def import_csv_file(filename):
    filename = os.path.basename(filename)
    
    file_path = global_util.get_full_path_input_file(filename)

    
    event_stream = csv_importer.import_event_stream(file_path)
    # dataframe = csv_import_adapter.import_dataframe_from_path(file_path, sep=",")

    
    log = conversion_factory.apply(event_stream, parameters={constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "日期和时间"})

    
    net, initial_marking, final_marking = alpha_miner.apply(log)

    
    gviz = visualizer.apply(net, initial_marking, final_marking)

    
    visualizer.view(gviz)


def test_import_xes_data(filename):
    filename = os.path.basename(filename)

    
    file_path = global_util.get_full_path_test_file(filename)

    
    log = importer.apply(file_path)
    for case_index, case in enumerate(log):
        print("\n case index: %d  case id: %s" % (case_index, case.attributes["concept:name"]))
        for event_index, event in enumerate(case):
            print("event index: %d  event activity: %s" % (event_index, event["concept:name"]))

    
    parameters = {"timestamp_sort": True}
    log = importer.apply(file_path, variant="nonstandard", parameters=parameters)
    for case_index, case in enumerate(log):
        print("\n case index: %d  case id: %s" % (case_index, case.attributes["concept:name"]))
        for event_index, event in enumerate(case):
            print("event index: %d  event activity: %s" % (event_index, event["concept:name"]))


if __name__ == "__main__":
    # test_import_xes_data("running.xes")
    import_xes_data("running.xes")
