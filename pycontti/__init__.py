import argparse

__version__ = "0.1.0"


def deploy_git(args):
    print(f"Deploying from git repository {args.url}")


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="sub-command help")

    parser_deploy_git = subparsers.add_parser("deploy-git")
    parser_deploy_git.add_argument("url", type=str, help="git url")
    parser.set_defaults(func=deploy_git)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    main()
