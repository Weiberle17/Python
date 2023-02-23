class Recording:
  def __init__(self, name, title, year):
    self.Name = name
    self.Title = title
    self.Year = year

  def edit(self):
    pass

  def delete(self):
    pass

  @staticmethod
  def convert(ganzzahl):
    hours = ganzzahl // 60
    minutes = (ganzzahl % 60)
    runtime = [hours, minutes]
    return runtime

class RecordingCD(Recording):
  type = "cd"
  def __init__(self, name, title, year):
    super().__init__(name, title, year)

class RecordingDownload(Recording):
  type = "download"
  def __init__(self, name, title, year):
    super().__init__(name, title, year)
