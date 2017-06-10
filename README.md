# keras-cntk-benchmark

Repository to benchmark the performance of the CNTK backend on Keras vs. the performance of TensorFlow.

## Usage

The repository uses my [keras-cntk-docker](https://github.com/minimaxir/keras-cntk-docker) container, and assumes necessary dependices for that are installed.

`keras_cntk_benchmark.py` contains the benchmark script.

`/test_files` contains the test files.

`/logs` contains the performance output (CSV) for each test.

`/analysis` contains the R Notebook + interactive data visualizations of the logs

## Maintainer

Max Woolf ([@minimaxir](http://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT