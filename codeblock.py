    \"\"\nEmbedded Python Blocks:\n\nEach time this file is saved,\
      \ GRC will instantiate the first class it finds\nto get ports and parameters\
      \ of your block. The arguments to __init__  will\nbe the parameters. All of\
      \ them are required to have default values!\n\"\"\"\n\nimport numpy as np\n\
      from gnuradio import gr\n\n\nclass blk(gr.sync_block):  # other base classes\
      \ are basic_block, decim_block, interp_block\n    \"\"\"Embedded Python Block\
      \ example - a simple multiply const\"\"\"\n\n    def __init__(self, example_param=1.0):\
      \  # only default arguments here\n        \"\"\"arguments to this function show\
      \ up as parameters in GRC\"\"\"\n        gr.sync_block.__init__(\n         \
      \   self,\n            name='Embedded Python Block',   # will show up in GRC\n\
      \            in_sig=[np.complex64],\n            out_sig=[np.complex64]\n  \
      \      )\n        # if an attribute with the same name as a parameter is found,\n\
      \        # a callback is registered (properties work, too).\n        self.example_param\
      \ = example_param\n\n    def work(self, input_items, output_items):\n      \
      \  \"\"\"example: multiply with constant\"\"\"\n        output_items[0][:] =\
      \ input_items[0] * self.example_param\n        return len(output_items[0])\n
