# Wallace
Wallace is a discord bot who likes cheesy music, only says the most inspirational platitudes and is often busy digging in to some wensleydale.

## Usage
To run wallace in your discord, you need to set up a discord bot (see for example [this tutorial](https://www.writebots.com/discord-bot-token/)) and get a token. Once you have downloaded this repo and and added it to your Python path, you can then run it with a script such as this:

    from wallace.wallace import Wallace
    wallace = Wallace()
    
    # Load modules
    from wallace.modules.cheese import CheeseModule
    wallace.load_module(CheeseModule)
    
    wallace.run("your-token-goes-here")
    
There are many more modules which can be loaded, or you can create your own modules by inheriting from `wallace.modules.base.basemodule.BaseModule` (or one of the other base modules provided in the `wallae.modules.base.basemodule` namespace).