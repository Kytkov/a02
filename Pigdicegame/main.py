# pylint: disable=C0103
"""Entry point for the Pig dice game application."""

import game as Game


def main() -> None:
    """Instantiate the game and start its main loop."""
    g = Game.Game()
    g.run()


if __name__ == "__main__":
    main()
