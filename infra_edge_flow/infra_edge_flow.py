from infra_edge_flow.api_flow.api_flow import APIFlow
from infra_edge_flow.ui_flow.ui_flow import UIFlow
from utils.text_utils import Utils


class InfraEdgeFlow():

    def __init__(self, page):
        self.page = page
        self.ui_flow = UIFlow(page)
        self.api_flow = APIFlow()
        self.utils = Utils()