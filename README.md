# Deployment

> Git-based deployment scripts

**Deploymnet** is a collection of git-based deployment scripts, written in Python, initially used for one
small and simple project, but turned into a complex and rich solution for deploying small and personal
projects of mine. It is not intended to be used in large, complex systems &mdash; ultimately, it's been used
for small contexts and scenarios. It is inspired in Heroku's deployment solutions and its CLI.

## Installing & Running

This is a Python pip package, so you're able to `pip install` it in your work environment. Basically,
it will install a `deployment` binary, which should be helpful to setup new projects.

```sh
$ pip install git+ssh://git@github.com/earaujoassis/deployment
```

Once the package is installed, you may run `deployment init` in order to setup a project. It will create
the necessary git-hooks and deployment scripts in the working directory. The `deployment setup` will attempt
to connect to the remote server and create the necessary information. If something is wrong or any necessary
information is needed, it will ask for it or raise any error. Once the `init` and `setup` steps are successfully
completed, you may run `deployment push` in order to deploy the current project to the remote upstream
(`deployment setup` will have created the necessary upstream for it).

If you need any help, please run `deployment help`.

## Developing

In order to create a sandbox (virtual environment) and install it for development or testing, you may run the
following commands:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install .
```

The `deployment` binary will be available in the current shell session.

## Issues

Please take a look at [/issues](https://github.com/earaujoassis/deployment/issues)

## License

[MIT License](http://earaujoassis.mit-license.org/) &copy; Ewerton Carlos Assis
