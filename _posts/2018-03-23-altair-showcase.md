---
layout: post
title: Altair 2.0 Showcase
embed-vega: true
permalink: /altair-showcase/
toc: true
---
![Altair Banner](/assets/images/altair-card-2.png)
When trying to explain [Altair](https://altair-viz.github.io/) to colleagues I find it's easier to show than tell. I have grabbed a
few highlights from the [example gallery](https://altair-viz.github.io/gallery/index.html) as a
quick reference. 


- [Basic Charts](#basic-charts)
- [Multivariate](#multivariate)
- [Geographic](#geographic)
- [Interactive](#interactive)

Note: All examples link to the source code.

## Basic Charts

[**Simple Scatter Plot**](https://altair-viz.github.io/gallery/scatter_tooltips.html):

{% capture scatter-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/cars.json",
    "format": {
      "type": "json"
    }
  },
  "mark": "point",
  "encoding": {
      "color": {"type": "nominal", "field": "Origin"},
    "tooltip": [
      {"type": "nominal", "field": "Name"},
      {"type": "nominal", "field": "Origin"},
      {"type": "quantitative", "field": "Horsepower"},
      {"type": "quantitative", "field": "Miles_per_Gallon"}
    ],
    "x": {"type": "quantitative", "field": "Horsepower"},
    "y": {"type": "quantitative", "field": "Miles_per_Gallon"}
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='scatter' spec=scatter-spec%}

[**Multi Series Line Chart**](https://altair-viz.github.io/gallery/multi_series_line.html):

{% capture stock-spec %}{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/stocks.csv",
    "format": {
      "type": "csv"
    }
  },
  "mark": "line",
  "encoding": {
    "color": {
      "type": "nominal",
      "field": "symbol"
    },
    "x": {
      "type": "temporal",
      "field": "date"
    },
    "y": {
      "type": "quantitative",
      "field": "price"
    }
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='stock' spec=stock-spec%}

[**Histogram**](https://altair-viz.github.io/gallery/simple_histogram.html):

{% capture hist-spec %}
{
  "config": {"view": {"continuousWidth": 400, "continuousHeight": 300}},
  "data": {
    "url": "https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/movies.json"
  },
  "mark": "bar",
  "encoding": {
    "x": {"type": "quantitative", "bin": true, "field": "IMDB_Rating"},
    "y": {"type": "quantitative", "aggregate": "count"}
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json"
}
{% endcapture %}
{% include vega-plot.html name='hist' spec=hist-spec%}

## Multivariate

[**Multifeature Scatter
Plot**](https://altair-viz.github.io/gallery/multifeature_scatter_plot.html):

{% capture iris-spec %}
{
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
  "config": {
    "view": {
      "height": 300,
      "width": 400
    }
  },
  "data": {
    "url": "https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/iris.json"
  },
  "encoding": {
    "color": {
      "field": "species",
      "type": "nominal"
    },
    "size": {
      "field": "petalWidth",
      "type": "quantitative"
    },
    "x": {
      "field": "sepalLength",
      "scale": {
        "zero": false
      },
      "type": "quantitative"
    },
    "y": {
      "field": "sepalWidth",
      "scale": {
        "padding": 1,
        "zero": false
      },
      "type": "quantitative"
    }
  },
  "mark": "circle"
}
{% endcapture %}
{% include vega-plot.html name='iris' spec=iris-spec%}

[**Trellis Stacked Bar Chart**](https://altair-viz.github.io/gallery/trellis_stacked_bar_chart.html)

{% capture barley-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/barley.json",
    "format": {
      "type": "json"
    }
  },
  "mark": "bar",
  "encoding": {
    "color": {
      "type": "nominal",
      "field": "site"
    },
    "column": {
      "type": "nominal",
      "field": "year"
    },
    "x": {
      "type": "quantitative",
      "aggregate": "sum",
      "field": "yield"
    },
    "y": {
      "type": "nominal",
      "field": "variety"
    }
  },
  "width": 250,
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='barley' spec=barley-spec%}


[**Table Bubble Plot**](https://altair-viz.github.io/gallery/table_bubble_plot_github.html):

{% capture github-spec %}{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/github.csv",
    "format": {
      "type": "csv"
    }
  },
  "mark": "circle",
  "encoding": {
    "color": {
      "type": "quantitative",
      "aggregate": "sum",
      "field": "count"
    },
    "size": {
      "type": "quantitative",
      "aggregate": "sum",
      "field": "count"
    },
    "x": {
      "type": "ordinal",
      "field": "time",
      "timeUnit": "hours"
    },
    "y": {
      "type": "ordinal",
      "field": "time",
      "timeUnit": "day"
    }
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='github' spec=github-spec%}


## Geographic

[**Choropleth Map**](https://altair-viz.github.io/gallery/choropleth.html):

{% capture choro-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/us-10m.json",
    "format": {
      "feature": "counties",
      "type": "topojson"
    }
  },
  "mark": "geoshape",
  "encoding": {
    "color": {
      "type": "quantitative",
      "field": "rate"
    }
  },
  "height": 300,
  "projection": {
    "type": "albersUsa"
  },
  "transform": [
    {
      "lookup": "id",
      "from": {
        "data": {
          "url": "https://vega.github.io/vega-datasets/data/unemployment.tsv",
          "format": {
            "type": "tsv"
          }
        },
        "key": "id",
        "fields": [
          "rate"
        ]
      }
    }
  ],
  "width": 500,
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='choro' spec=choro-spec%}


[**London Tube Lines**](https://altair-viz.github.io/gallery/london_tube.html):

{% capture london-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "layer": [
    {
      "data": {
        "url": "https://vega.github.io/vega-datasets/data/londonBoroughs.json",
        "format": {
          "feature": "boroughs",
          "type": "topojson"
        }
      },
      "mark": {
        "type": "geoshape",
        "stroke": "white",
        "strokeWidth": 2
      },
      "encoding": {
        "color": {
          "value": "#eee"
        }
      },
      "height": 500,
      "width": 700
    },
    {
      "data": {
        "url": "https://vega.github.io/vega-datasets/data/londonCentroids.json",
        "format": {
          "type": "json"
        }
      },
      "mark": "text",
      "encoding": {
        "latitude": {
          "type": "quantitative",
          "field": "cy"
        },
        "longitude": {
          "type": "quantitative",
          "field": "cx"
        },
        "opacity": {
          "value": 0.6
        },
        "size": {
          "value": 8
        },
        "text": {
          "type": "nominal",
          "field": "bLabel"
        }
      },
      "transform": [
        {
          "calculate": "indexof (datum.name,' ') > 0  ? substring(datum.name,0,indexof(datum.name, ' ')) : datum.name",
          "as": "bLabel"
        }
      ]
    },
    {
      "data": {
        "url": "https://vega.github.io/vega-datasets/data/londonTubeLines.json",
        "format": {
          "feature": "line",
          "type": "topojson"
        }
      },
      "mark": {
        "type": "geoshape",
        "filled": false,
        "strokeWidth": 2
      },
      "encoding": {
        "color": {
          "type": "nominal",
          "field": "id",
          "legend": {
            "offset": 0,
            "orient": "bottom-right",
            "title": null
          }
        }
      }
    }
  ],
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='london' spec=london-spec%}


[**One Dot Per Zipcode**](https://altair-viz.github.io/gallery/one_dot_per_zipcode.html):

{% capture zipcode-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/zipcodes.csv",
    "format": {
      "type": "csv"
    }
  },
  "mark": {
    "type": "circle",
    "size": 3
  },
  "encoding": {
    "color": {
      "type": "nominal",
      "field": "digit"
    },
    "latitude": {
      "type": "quantitative",
      "field": "latitude"
    },
    "longitude": {
      "type": "quantitative",
      "field": "longitude"
    }
  },
  "height": 400,
  "projection": {
    "type": "albersUsa"
  },
  "transform": [
    {
      "calculate": "substring(datum.zip_code,0,1)",
      "as": "digit"
    }
  ],
  "width": 650,
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='zipcode' spec=zipcode-spec%}

## Interactive

[**Dot Dash Plot**](https://altair-viz.github.io/gallery/dot_dash_plot.html):
Click and drag on the scatter plot to highlight a region. The selection can be dragged as well.
{% capture dotdash-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "hconcat": [
    {
      "data": {
        "url": "https://vega.github.io/vega-datasets/data/cars.json",
        "format": {
          "type": "json"
        }
      },
      "mark": "tick",
      "encoding": {
        "color": {
          "condition": {
            "type": "nominal",
            "field": "Origin",
            "selection": "selector003"
          },
          "value": "lightgrey"
        },
        "x": {
          "type": "nominal",
          "axis": {
            "domain": false,
            "labels": false,
            "ticks": false,
            "title": ""
          },
          "field": "Origin"
        },
        "y": {
          "type": "quantitative",
          "axis": {
            "domain": false,
            "labels": false,
            "ticks": false
          },
          "field": "Horsepower"
        }
      },
      "selection": {
        "selector003": {
          "type": "interval",
          "on": "[mousedown, window:mouseup] > window:mousemove!",
          "encodings": [
            "x",
            "y"
          ],
          "translate": "[mousedown, window:mouseup] > window:mousemove!",
          "zoom": "wheel!",
          "mark": {
            "fill": "#333",
            "fillOpacity": 0.125,
            "stroke": "white"
          },
          "resolve": "global"
        }
      }
    },
    {
      "vconcat": [
        {
          "data": {
            "url": "https://vega.github.io/vega-datasets/data/cars.json",
            "format": {
              "type": "json"
            }
          },
          "mark": "point",
          "encoding": {
            "color": {
              "condition": {
                "type": "nominal",
                "field": "Origin",
                "selection": "selector003"
              },
              "value": "grey"
            },
            "x": {
              "type": "quantitative",
              "axis": {
                "title": ""
              },
              "field": "Miles_per_Gallon"
            },
            "y": {
              "type": "quantitative",
              "axis": {
                "title": ""
              },
              "field": "Horsepower"
            }
          },
          "selection": {
            "selector003": {
              "type": "interval",
              "on": "[mousedown, window:mouseup] > window:mousemove!",
              "encodings": [
                "x",
                "y"
              ],
              "translate": "[mousedown, window:mouseup] > window:mousemove!",
              "zoom": "wheel!",
              "mark": {
                "fill": "#333",
                "fillOpacity": 0.125,
                "stroke": "white"
              },
              "resolve": "global"
            }
          }
        },
        {
          "data": {
            "url": "https://vega.github.io/vega-datasets/data/cars.json",
            "format": {
              "type": "json"
            }
          },
          "mark": "tick",
          "encoding": {
            "color": {
              "condition": {
                "type": "nominal",
                "field": "Origin",
                "selection": "selector003"
              },
              "value": "lightgrey"
            },
            "x": {
              "type": "quantitative",
              "axis": {
                "domain": false,
                "labels": false,
                "ticks": false
              },
              "field": "Miles_per_Gallon"
            },
            "y": {
              "type": "nominal",
              "axis": {
                "domain": false,
                "labels": false,
                "ticks": false,
                "title": ""
              },
              "field": "Origin"
            }
          },
          "selection": {
            "selector003": {
              "type": "interval",
              "on": "[mousedown, window:mouseup] > window:mousemove!",
              "encodings": [
                "x",
                "y"
              ],
              "translate": "[mousedown, window:mouseup] > window:mousemove!",
              "zoom": "wheel!",
              "mark": {
                "fill": "#333",
                "fillOpacity": 0.125,
                "stroke": "white"
              },
              "resolve": "global"
            }
          }
        }
      ]
    }
  ],
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='dotdash' spec=dotdash-spec%}

[**US Population Over Time**](https://altair-viz.github.io/gallery/us_population_over_time.html):
Sliders allow for selections to be varied

{% capture population-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/population.json",
    "format": {
      "type": "json"
    }
  },
  "mark": "bar",
  "encoding": {
    "color": {
      "type": "nominal",
      "field": "sex",
      "scale": {
        "domain": [
          "Male",
          "Female"
        ],
        "range": [
          "steelblue",
          "salmon"
        ]
      }
    },
    "column": {
      "type": "ordinal",
      "field": "age"
    },
    "x": {
      "type": "nominal",
      "axis": {
        "title": null
      },
      "field": "sex"
    },
    "y": {
      "type": "quantitative",
      "field": "people",
      "scale": {
        "domain": [
          0,
          12000000
        ]
      }
    }
  },
  "selection": {
    "year": {
      "type": "single",
      "fields": [
        "year"
      ],
      "bind": {
        "input": "range",
        "max": 2000,
        "min": 1900,
        "step": 10
      },
      "on": "click",
      "resolve": "global",
      "empty": "all"
    }
  },
  "transform": [
    {
      "calculate": "if((datum.sex === 1),'Male','Female')",
      "as": "sex"
    },
    {
      "filter": {
        "selection": "year"
      }
    }
  ],
  "width": 20,
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='population' spec=population-spec%}

[**Seattle Weather Interactive**](https://altair-viz.github.io/gallery/seattle_weather_interactive.html):
Click and drag on the scatter plot for a filtered histogram. Click on the histogram bars for a
filtered scatter plot. Shift-Click for mulitple bars.

{% capture weather-spec %}
{
  "config": {
    "view": {
      "width": 400,
      "height": 300
    }
  },
  "vconcat": [
    {
      "mark": "point",
      "encoding": {
        "color": {
          "condition": {
            "type": "nominal",
            "field": "weather",
            "scale": {
              "domain": [
                "sun",
                "fog",
                "drizzle",
                "rain",
                "snow"
              ],
              "range": [
                "#e7ba52",
                "#a7a7a7",
                "#aec7e8",
                "#1f77b4",
                "#9467bd"
              ]
            },
            "selection": "selector014"
          },
          "value": "lightgray"
        },
        "size": {
          "type": "quantitative",
          "field": "precipitation",
          "scale": {
            "range": [
              5,
              200
            ]
          }
        },
        "x": {
          "type": "temporal",
          "axis": {
            "title": "Date"
          },
          "field": "date",
          "timeUnit": "monthdate"
        },
        "y": {
          "type": "quantitative",
          "axis": {
            "title": "Maximum Daily Temperature (C)"
          },
          "field": "temp_max",
          "scale": {
            "domain": [
              -5,
              40
            ]
          }
        }
      },
      "height": 300,
      "selection": {
        "selector014": {
          "type": "interval",
          "encodings": [
            "x"
          ],
          "on": "[mousedown, window:mouseup] > window:mousemove!",
          "translate": "[mousedown, window:mouseup] > window:mousemove!",
          "zoom": "wheel!",
          "mark": {
            "fill": "#333",
            "fillOpacity": 0.125,
            "stroke": "white"
          },
          "resolve": "global"
        }
      },
      "transform": [
        {
          "filter": {
            "selection": "selector015"
          }
        }
      ],
      "width": 600
    },
    {
      "mark": "bar",
      "encoding": {
        "color": {
          "condition": {
            "type": "nominal",
            "field": "weather",
            "scale": {
              "domain": [
                "sun",
                "fog",
                "drizzle",
                "rain",
                "snow"
              ],
              "range": [
                "#e7ba52",
                "#a7a7a7",
                "#aec7e8",
                "#1f77b4",
                "#9467bd"
              ]
            },
            "selection": "selector015"
          },
          "value": "lightgray"
        },
        "x": {
          "type": "quantitative",
          "aggregate": "count",
          "field": "*"
        },
        "y": {
          "type": "nominal",
          "field": "weather"
        }
      },
      "selection": {
        "selector015": {
          "type": "multi",
          "encodings": [
            "color"
          ],
          "on": "click",
          "toggle": "event.shiftKey",
          "resolve": "global",
          "empty": "all"
        }
      },
      "transform": [
        {
          "filter": {
            "selection": "selector014"
          }
        }
      ],
      "width": 600
    }
  ],
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/seattle-weather.csv",
    "format": {
      "type": "csv"
    }
  },
  "title": "Seattle Weather: 2012-2015",
  "$schema": "https://vega.github.io/schema/vega-lite/v2.json"
}
{% endcapture %}
{% include vega-plot.html name='weather' spec=weather-spec%}


{% capture generic-spec %}
{% endcapture %}
{% include vega-plot.html name='generic' spec=generic-spec%}
