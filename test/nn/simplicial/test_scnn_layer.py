"""Test the SCNN layer."""

import torch

from topomodelx.nn.simplicial.scnn_layer import SCNNLayer


class TestSCNNLayer:
    """Test the SCNN layer."""

    def test_forward(self):
        """Test the forward pass of the SCNN layer."""
        in_channels = 5
        out_channels = 5
        conv_order_down = 3
        conv_order_up = 3
        
        n_simplices = 10 
        laplacian_down = torch.randint(0, 2, (n_simplices, n_simplices)).float()
        laplacian_up = torch.randint(0, 2, (n_simplices, n_simplices)).float()
        x = torch.randn(n_simplices, in_channels)

        # Without aggregation normalization, without update function 
        scnn = SCNNLayer(in_channels, out_channels, conv_order_down,
                         conv_order_up,
                         aggr_norm=False,
                         update_func=None,)
        output = scnn.forward(x, laplacian_down=laplacian_down,
                              laplacian_up=laplacian_up)

        assert output.shape == (n_simplices, out_channels)

        # Without aggregation normalization, With update function 
        scnn = SCNNLayer(in_channels, out_channels, conv_order_down,
                         conv_order_up,
                         aggr_norm=False,
                         update_func='sigmoid',)
        output = scnn.forward(x, laplacian_down=laplacian_down,
                              laplacian_up=laplacian_up)

        assert output.shape == (n_simplices, out_channels)

        # With aggregation normalization, with update function 
        scnn = SCNNLayer(in_channels, out_channels, conv_order_down,
                         conv_order_up,
                         aggr_norm=True,
                         update_func='sigmoid',)
        output = scnn.forward(x, laplacian_down=laplacian_down,
                              laplacian_up=laplacian_up)

        assert output.shape == (n_simplices, out_channels)
