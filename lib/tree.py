class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      # 1. Remove the first node from the `nodes_to_visit` list
      node = nodes_to_visit.pop(0)
      # 2. Add its value to the result list
      result.append(node['id'])
      if node['id'] == id:
        return node
      else:
      # 3. Add its children (if any) to the BEGINNING of the `nodes_to_visit` list
        nodes_to_visit = node['children'] + nodes_to_visit

