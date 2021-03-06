#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("switching to test mode")
        os.environ["DJANGO_SETTINGS_MODULE"] = "config.test"

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
        
    # This allows easy placement of apps within the interior apps directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "apps"))    

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
