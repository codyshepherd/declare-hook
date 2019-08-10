# Declare-Hooks

This is a tool for compiling a custom LiveCD-Rootfs build hook from a yaml file
and a series of shell gadget templates.

In your configuration yaml (see `img.yaml` for an example), specify the gadget
templates you would like to include in your script, in order, under the
`templates:` key.

Values for the jinja2 variables present in those gadget templates should be
specified in your yaml configuration.

## Install

* Create a python3 virtualenvironment
* `pip install .`

## Use

`declare-hook myconfig.yaml`

This will create a hook called `output.binary` in the project directory, which
can then be placed in a subdirectory of livecd-rootfs `hooks.d/`, and built
with livecd-rootfs, likely via a tool like
[ubuntu old fashioned](https://github.com/chrisglass/ubuntu-old-fashioned)
